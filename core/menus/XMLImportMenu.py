import os

from core.classes.EventXMLImporter import EventXMLImporter
from core.classes.MatchXMLImporter import MatchXMLImporter
from core.colorama import init, Fore

init()

class XMLImportMenu:

    def __init__(self, TESTING):
        self.TESTING = TESTING
        self.running = True

    def run(self, match):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('+------------------------------------+')
            print('| XML Files Importer                 |')
            print('| Please follow the instructions     |')
            print('+------------------------------------+\n')
            match = self.__importMatchData(match)
            match = self.__importEventData(match)
            self.running = False

        return match

    def __importMatchData(self, match):
        if self.TESTING:
            path = "./data/match.xml"
        else:
            path = input('Please enter the relative path to the match data XML file: ')
        matchImporter = MatchXMLImporter(path)
        print('Adding teams to the match... ', '')
        for team in matchImporter.getTeamElements():
            match._addTeam(team)
        print(Fore.BLUE + "Done" + Fore.WHITE)
        print('Adding players to the match and teams... ', '')
        for player in matchImporter.getPlayers():
            match._addPlayer(player)
        print(Fore.BLUE + "Done" + Fore.WHITE)

        return match

    def __importEventData(self, match):
        if self.TESTING:
            path = "./data/events.xml"
        else:
            path = input('Please enter the relative path to the event data XML file: ')
        eventImporter = EventXMLImporter(path, match)
        print(Fore.WHITE + 'Adding events to the match, teams and players... ', '')
        for event in eventImporter.getEvents(match):
            match._addEvent(event)
        print(Fore.BLUE + "Done" + Fore.WHITE)
        return match