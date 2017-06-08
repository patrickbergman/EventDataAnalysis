class Match:

    def __init__(self):
        self.teams = []

    def add_team(self, team):
        """Add a team to the match"""
        self.teams.append(team)

    def findTeamById(self, teamId, default=None):
        """return a team from the array"""
        for team in self.teams:
            if team.getId() == teamId:
                return team

        return default