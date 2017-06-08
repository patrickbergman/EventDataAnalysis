class Team:

    def __init__(self, teamId):
        self.__teamId = teamId
        self.__country = ''
        self.__name = ''
        self.__score = ''
        self.__side = ''

    def getId(self):
        return self.__teamId

    def getName(self):
        return self.__name

    def setCountry(self, countryName):
        self.__country = countryName

    def setName(self, teamName):
        self.__name = teamName

    def setScore(self, teamScore):
        self.__score = teamScore

    def setSide(self, teamSide):
        self.__side = teamSide