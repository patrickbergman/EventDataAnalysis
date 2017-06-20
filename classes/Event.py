class Event:

    def __init__(self, id, eventId, typeId, periodId, min, sec, teamId, outcome, x, y, timestamp):
        self.__qualifiers = []
        self.__id = id
        self.__eventId = eventId
        self.__typeId = typeId
        self.__periodId = periodId
        self.__min = min
        self.__sec = sec
        self.__teamId = teamId
        self.__outcome = outcome
        self.__x = x
        self.__y = y
        self.__timestamp = timestamp
        self.__playerId = ''

    def getId(self):
        return self.__id

    def getEventId(self):
        return self.__eventId

    def getTypeId(self):
        return self.__typeId

    def getPeriodId(self):
        return self.__periodId

    def getMinute(self):
        return self.__min

    def getSecond(self):
        return self.__sec

    def getTeamId(self):
        return self.__teamId

    def getOutcome(self):
        return self.__outcome

    def getXCoordinate(self):
        return self.__x

    def getYCoordinate(self):
        return self.__y

    def getTimestamp(self):
        return self.__timestamp

    def hasPlayerId(self):
        return self.__playerId != ''

    def getPlayerId(self):
        return self.__playerId

    def _setPlayerId(self, playerId):
        self.__playerId = playerId

    def _addQualifier(self, qualifier):
        self.__qualifiers.append(qualifier)