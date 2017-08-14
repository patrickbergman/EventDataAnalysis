import os

from core.classes.Match import Match

from core.classes.EventXMLImporter import EventXMLImporter
from core.classes.MatchXMLImporter import MatchXMLImporter
from core.colorama import init, Fore

init()

class XMLImportMenu:

    def __init__(self, TESTING):
        self.TESTING = TESTING
        self.running = True
        self.multiple = False

    # returns a match if single match, otherwise list of matches with common teamcode at match[0]
    def run(self, match):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('+------------------------------------+')
            print('| XML Files Importer                 |')
            print('| Please follow the instructions     |')
            print('+------------------------------------+\n')
            if self.multiple:
                match = self.__importMultiple()
            else:
                match = self.__importMatchData(match)
                match = self.__importEventData(match)
            self.running = False

        return match

    def __importMultiple(self):
        matchList = [""]
        iterator = 1
        basepath = os.path.join(os.getcwd(),"data")
        for entry in os.listdir(basepath):
            path = os.path.join(basepath, entry)
            if os.path.isdir(path):
                match = Match()
                match = self.__importMultipleMatchData(match, path)
                match = self.__importMultipleEventData(match, path)
                matchList.append(match)

        # find common team and put on matchList[0]
        teamlist1 = matchList[1].getTeams()
        teamlist2 = matchList[2].getTeams()
        if teamlist1[0].getId() == teamlist2[0].getId() or teamlist1[0].getId() == teamlist2[1].getId():
            matchList[0] = teamlist1[0].getId()
        else:
            matchList[0] = teamlist1[1].getId()

        return matchList

    def __importMultipleMatchData(self, match, initPath):
        path = os.path.join(initPath, 'match.xml')
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

    def __importMultipleEventData(self, match, initPath):
        path = os.path.join(initPath, 'events.xml')
        eventImporter = EventXMLImporter(path, match)
        print(Fore.WHITE + 'Adding events to the match, teams and players... ', '')
        for event in eventImporter.getEvents(match):
            match._addEvent(event)
        print(Fore.BLUE + "Done" + Fore.WHITE)
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