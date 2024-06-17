class Result:
    def __init__(self, result: list):
        self.team_home = result[0]
        self.team_away = result[1]
        self.goals_home = result[2]
        self.goals_away = result[3]
