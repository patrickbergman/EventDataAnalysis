class Qualifier:

    def __init__(self, id, qualifierId):
        self.__id = id
        self.__qualifierId = qualifierId
        self.__value = ''

    def _setValue(self, value):
        self.__value = value