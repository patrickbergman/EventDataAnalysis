class Team:

    def __init__(self, teamId):
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