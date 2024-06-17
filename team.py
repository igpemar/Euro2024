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
