euro_qualifier_ranking = {
    "Belgium": 1,
    "Italy": 2,
    "England": 3,
    "Germany": 4,
    "Spain": 5,
    "Ukraine": 6,
    "France": 7,
    "Poland": 8,
    "Switzerland": 9,
    "Croatia": 10,
    "Netherlands": 11,
    "Portugal": 12,
    "Turkey": 13,
    "Denmark": 14,
    "Austria": 15,
    "Hungary": 16,
    "Czechia": 17,
    "Serbia": 18,
    "Slovakia": 19,
    "Scotland": 20,
    "Slovenia": 21,
    "Romania": 22,
    "Georgia": 23,
    "Albania": 24,
}


class Team:
    def __init__(self, name: str, group_name: str):
        self.name = name
        self.points = 0
        self.PG = 0
        self.GS = 0
        self.GA = 0
        self.GD = 0
        self.W = 0
        self.rank = 0
        self.group = group_name
        self.head_to_head = {}
        self.euro_qualifier_ranking = euro_qualifier_ranking[name]

    def update_stats_home(self, result):
        self.PG += 1
        self.GS += result.goals_home
        self.GA += result.goals_away
        self.GD = self.GS - self.GA
        if result.goals_home > result.goals_away:
            self.points += 3
            self.W += 1
            self.head_to_head[result.team_away] = "W"
        elif result.goals_home < result.goals_away:
            self.head_to_head[result.team_away] = "L"
        else:
            self.points += 1
            self.head_to_head[result.team_away] = "D"

    def update_stats_away(self, result):
        self.PG += 1
        self.GS += result.goals_away
        self.GA += result.goals_home
        self.GD = self.GS - self.GA
        if result.goals_away > result.goals_home:
            self.points += 3
            self.W += 1
            self.head_to_head[result.team_home] = "W"
        elif result.goals_home > result.goals_away:
            self.head_to_head[result.team_home] = "L"
        else:
            self.points += 1
            self.head_to_head[result.team_home] = "D"
