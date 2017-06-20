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

    def _setPlayerId(self, playerId):
        self.__playerId = playerId

    def _addQualifier(self, qualifier):
        self.__qualifiers.append(qualifier)