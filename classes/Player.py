class Team:

    def __init__(self, playerId, position, shirt_number, status):
        self.__playerId = playerId
        self.__position = position
        self.__shirtNumber = shirt_number
        self.__status = status
        self.__subPosition = ''
        self.__firstName = ''
        self.__lastName = ''
        self.__knownName = ''

    def setSubPosition(self, sub_position):
        self.__subPosition = sub_position

    def setFirstName(self, first_name):
        self.__firstName = first_name

    def setLastName(self, last_name):
        self.__lastName = last_name

    def setKnownName(self, known_name):
        self.__knownName = known_name