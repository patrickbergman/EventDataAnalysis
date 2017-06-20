class Match:

    def __init__(self):
        self.__teams = []
        self.__players = []

    def addTeam(self, team):
        """Add a team to the match"""
        self.__teams.append(team)

    def addPlayer(self, player):
        """Add a player to the match and the team"""
        self.__players.append(player)
        self.__addPlayerToTeam(player, player.getTeamId())

    def findTeamById(self, teamId, default=None):
        """return a team from the array"""
        for team in self.__teams:
            if team.getId() == teamId:
                return team
        return default

    def getTeams(self):
        return self.__teams

    def getPlayers(self):
        return self.__players

    def __addPlayerToTeam(self, player, teamId):
        """Add a player to his/her team"""
        team = self.findTeamById(teamId)
        team.addPlayer(player)