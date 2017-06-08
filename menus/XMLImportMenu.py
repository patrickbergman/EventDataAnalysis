import os
from classes.MatchXMLImporter import MatchXMLImporter


class XMLImportMenu:

    def __init__(self):
        self.running = True

    def run(self, match):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('+------------------------------------+')
            print('| XML Files Importer                 |')
            print('| Please follow the instructions     |')
            print('+------------------------------------+\n')
            match = self.__importMatchData(match)
            # self.__importEventData()
            self.running = False

        return match

    def __importMatchData(self, match):
        path = input('Please enter the relative path to the match data XML file: ')
        matchImporter = MatchXMLImporter(path)
        for team in matchImporter.getTeamElements():
            match.add_team(team)

        return match