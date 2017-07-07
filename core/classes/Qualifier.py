class Qualifier:

    def __init__(self, qId, qualifierId):
        self.__id = qId
        self.__qualifierId = int(qualifierId)
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