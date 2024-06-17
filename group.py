import pandas as pd
import calendars, team, result


def initialize():
    groups = []
    groups.append(Group("A", calendars.calendarA))
    groups.append(Group("B", calendars.calendarB))
    # groups.append(Group("C", calendars.calendarC))
    # groups.append(Group("D", calendars.calendarD))
    # groups.append(Group("E", calendars.calendarE))
    # groups.append(Group("F", calendars.calendarF))
    return groups


class Group:
    def __init__(self, name: str, calendar: list[list[team.Team]]):
        self.name = name
        self.teams = self.set_teams(calendar)
        self.calendar = self.set_calendar(calendar)
        self.results = self.get_results_from_played_matches(calendar)
        self.standings = self.calculate_standings()

    def set_calendar(self, calendar):
        return [[match[0], match[1]] for match in calendar]

    def set_teams(self, calendar: list[list[team.Team]]) -> dict:
        matches = list(
            set([team for match in calendar for team in match if isinstance(team, str)])
        )
        dict = {}
        for teamStr in matches:
            team_obj = team.Team(teamStr, self.name)
            dict[team_obj.name] = team_obj
        return dict

    def get_results_from_played_matches(self, calendar):
        return {
            self.match_tag(match[0], match[1]): result.Result(match)
            for match in calendar
            if match[2] != -1
        }

    def simulate(self, fn):
        for match in self.calendar:
            match_tag = self.match_tag(match[0], match[1])
            if match_tag in self.results:
                continue
            self.results[match_tag] = result.Result([match[0], match[1], *fn(match)])

    def update_team_stats(self):
        for _, result in self.results.items():
            self.teams[result.team_home].update_stats_home(result)
            self.teams[result.team_away].update_stats_away(result)

    def calculate_standings(self):
        # If two or more teams finish level on points in a group, the following tie-break criteria
        # : apply
        # 1. Number of points obtained in the match(es) played between the teams in question
        # 2. Superior goal difference in the match(es) played between the teams in question
        # 3. Number of goals scored in the match(es) played between the teams in question
        # In the event of a three-way tie, where criteria 1-3 have managed to break the tie for only
        # team, they are applied again but this time only to the match between the two remaining
        # tied teams. If after this any tie still remains, we move on to the following:
        # 1. Superior goal difference in all group games
        # 2. Number of goals scored in all group matches
        self.update_team_stats()
        data = {
            "Team.Name": [team.name for team in self.teams.values()],
            "Team.PG": [team.PG for team in self.teams.values()],
            "Team.GS": [team.GS for team in self.teams.values()],
            "Team.GA": [team.GA for team in self.teams.values()],
            "Team.GD": [team.GD for team in self.teams.values()],
            "Team.Points": [team.points for team in self.teams.values()],
        }
        # Creating DataFrame
        df = pd.DataFrame(data)
        # Sorting DataFrame by points
        df = df.sort_values(by=["Team.Points"], ascending=False, ignore_index=True)
        # Check for ties in points and apply tie breaking criteria in case of equal number of points
        for i, team_name in enumerate(df["Team.Name"][:-1]):
            if df.iloc[i]["Team.Points"] == df.iloc[i + 1]["Team.Points"]:
                team_lag = team_name
                team_lead = df.iloc[i + 1]["Team.Name"]
                # First Tie break
                ## Lag team won in head to head match
                if self.first_tie_break(team_lag, team_lead) == "W":
                    continue
                ## Lag team lost in head to head match
                if self.first_tie_break(team_lag, team_lead) == "L":
                    df.iloc[[i, i + 1]] = df.iloc[[i + 1, i]].values
                    continue
                ## Head to head match was a draw

                # Second Tie break
                ## Lag team has a greater goal difference
                if self.second_tie_break(df, i, i + 1) == 1:
                    continue
                ## Lag team has a lower goal difference
                if self.second_tie_break(df, i, i + 1) == -1:
                    df.iloc[[i, i + 1]] = df.iloc[[i + 1, i]].values
                    continue
                ## Lag team and lead team have the same goal difference

                # Third tie break
                ## Lag team has scored more overall goals
                if self.third_tie_break(df, i, i + 1) == 1:
                    continue
                ## Lag team has scored less overall goals
                if self.third_tie_break(df, i, i + 1) == -1:
                    df.iloc[[i, i + 1]] = df.iloc[[i + 1, i]].values
                    continue

        df["Rank"] = df.index + 1
        return df

    def calculate_standings_3rd_group(self):
        # The six third-place finishers will be placed into a separate league table to determine the
        # four qualifiers for the next stage. Clearly no head-to-head angle here, so the rules for
        # classification are straightforward:
        # Points
        # Goal difference
        # Goals scored
        # Wins
        # Disciplinary points total (see above)
        # European Qualifiers ranking or drawing lots if Germany are involved
        self.update_team_stats()
        data = {
            "Team.Name": [team.name for team in self.teams.values()],
            "Team.Points": [team.points for team in self.teams.values()],
            "Team.GD": [team.GD for team in self.teams.values()],
            "Team.GS": [team.GS for team in self.teams.values()],
            "Team.GA": [team.GA for team in self.teams.values()],
            "Team.W": [team.W for team in self.teams.values()],
            "Team.PG": [team.PG for team in self.teams.values()],
        }
        # Creating DataFrame
        df = pd.DataFrame(data)
        # Sorting DataFrame by points
        df = df.sort_values(
            by=["Team.Points", "Team.GD", "Team.GS", "Team.W"],
            ascending=False,
            ignore_index=True,
        )
        df["Rank"] = df.index + 1
        return df

    def first_tie_break(self, team_lag, team_lead):
        return self.teams[team_lag].head_to_head.get(team_lead, 0)

    def second_tie_break(self, df, i_lag, i_lead):
        if df.iloc[i_lag]["Team.GD"] > df.iloc[i_lead]["Team.GD"]:
            return 1
        if df.iloc[i_lag]["Team.GD"] < df.iloc[i_lead]["Team.GD"]:
            return -1
        return 0

    def third_tie_break(self, df, i_lag, i_lead):
        if df.iloc[i_lag]["Team.GS"] > df.iloc[i_lead]["Team.GS"]:
            return 1
        if df.iloc[i_lag]["Team.GS"] < df.iloc[i_lead]["Team.GS"]:
            return -1
        return 0

    def update_standings(self):
        self.standings = self.calculate_standings()

    def update_standings_3rd_group(self):
        self.standings = self.calculate_standings_3rd_group()

    def update_standings_3rd_group(self):
        self.standings = self.calculate_standings_3rd_group()

    def match_tag(self, team_home, team_away):
        return f"{team_home}-{team_away}"

    def qualifies(
        self, ranks: list[int] = [1, 2], override_tag: bool = False
    ) -> list[str]:
        qualified = {}
        for rank in ranks:
            team_group_name = self.teams[
                self.standings.iloc[rank - 1]["Team.Name"]
            ].group

            tag = f"{rank}{team_group_name}"
            if override_tag:
                tag = f"3{team_group_name}"
            qualified[tag] = self.teams[self.standings.iloc[rank - 1]["Team.Name"]]
        return qualified
