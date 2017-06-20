class Qualifier:

    def __init__(self, id, qualifierId):
        self.__id = id
        self.__qualifierId = qualifierId
        self.__value = ''

    def getId(self):
        return self.__id

    def getQualifierId(self):
        return self.__qualifierId

    def hasValue(self):
        return self.__value != ''

    def getValue(self):
        return self.__value

    def _setValue(self, value):
        self.__value = value