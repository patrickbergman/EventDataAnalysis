class Match:

    def __init__(self):
        self.__teams = []
        self.__players = []
        self.__events = []

    def findTeamById(self, teamId, default=None):
        """return a team from the array"""
        for team in self.__teams:
            if team.getId() == teamId:
                return team
        return default

    def findPlayerById(self, playerId, default=None):
        """return a player from the array"""
        for player in self.__players:
            if player.getId() == playerId:
                return player
        return default

    def getTeams(self):
        return self.__teams

    def getPlayers(self):
        return self.__players

    def _addTeam(self, team):
        """Add a team to the match"""
        self.__teams.append(team)

    def _addEvent(self, event):
        """Add an event to the match, teams and players"""
        self.__events.append(event)
        self.findTeamById(event.getTeamId())._addEvent(event)
        if event.hasPlayerId():
            self.findPlayerById(event.getPlayerId())._addEvent(event)

    def _addPlayer(self, player):
        """Add a player to the match and the team"""
        self.__players.append(player)
        self.__addPlayerToTeam(player, player.getTeamId())

    def __addPlayerToTeam(self, player, teamId):
        """Add a player to his/her team"""
        team = self.findTeamById(teamId)
        team._addPlayer(player)