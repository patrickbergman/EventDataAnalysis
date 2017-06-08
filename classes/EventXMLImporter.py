import xml.etree.ElementTree as ET

class EventXMLImporter:

    def __init__(self, path):
        self.path = path
        self.checkXMLFile()

    def checkXMLFile(self):
        " Checks if the XML file is correctly formatted "