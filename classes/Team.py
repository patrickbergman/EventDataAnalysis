class Team:

    def __init__(self, teamId):
        self.__events = []
        self.__teamId = teamId
        self.__country = ''
        self.__name = ''
        self.__score = ''
        self.__side = ''
        self.__players = []

    def getId(self):
        return self.__teamId

    def getName(self):
        return self.__name

    def findPlayerById(self, playerId, default=None):
        """return a player from the array"""
        for player in self.__players:
            if player.getId() == playerId:
                return player
        return default

    def _setCountry(self, countryName):
        self.__country = countryName

    def _setName(self, teamName):
        self.__name = teamName

    def _setScore(self, teamScore):
        self.__score = teamScore

    def _setSide(self, teamSide):
        self.__side = teamSide

    def _addPlayer(self, player):
        self.__players.append(player)

    def _addEvent(self, event):
        self.__events.append(event)
        if event.hasPlayerId():
            self.findPlayerById(event.getPlayerId())._addEvent(event)