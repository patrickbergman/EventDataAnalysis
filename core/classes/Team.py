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

    def getPlayers(self):
        return self.__players

    def getEvents(self):
        return self.__events

    def findPlayerById(self, playerId, default=None):
        """return a player from the array"""
        for player in self.__players:
            if player.getId() == playerId:
                return player
        return default

    def findEventsByQualifierId(self, qId):
        """return all events with a certain qualifier id"""
        events = []
        for event in self.__events:
            if event.findQualifierByQualifierId(qId) is not None:
                events.append(event)
        return events

    def getEventsByTypeId(self, typeId):
        if type(typeId) is int:
            typeId = str(typeId)
        events = []
        for event in self.__events:
            if event.getTypeId() == typeId:
                events.append(event)
        return events

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