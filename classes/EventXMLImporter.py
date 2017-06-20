import xml.etree.ElementTree as ET
from colorama import init, Fore
from classes.Event import Event
from classes.Qualifier import Qualifier
init()

class EventXMLImporter:

    def __init__(self, path, match):
        self.path = path
        self.match = match
        self.root = ''
        self.__loadXMLFile()
        self.__checkXMLFile()

    ###########################################
    ## functions for returning elements      ##
    ###########################################

    def getEvents(self, match):
        """ Returns an array with events and their qualifiers """
        events = []
        for game in self.root.iterfind('Game'):
            for event in game.iterfind('Event'):
                tempEvent = Event(event.get('id'), event.get('event_id'), event.get('type_id'), event.get('period_id'), event.get('min'), event.get('sec'), "t" + event.get('team_id'), event.get('outcome'), event.get('x'), event.get('y'), event.get('timestamp'))
                if event.get('player_id') is not None:
                    tempEvent._setPlayerId("p" + event.get('player_id'))
                    tempEvent._setPlayer(match.findPlayerById("p" + event.get('player_id')))
                if event.find('Q') is not None:
                    for qualifier in event.iterfind('Q'):
                        tempQ = Qualifier(qualifier.get('id'), qualifier.get('qualifier_id'))
                        if qualifier.get('value') is not None:
                            tempQ._setValue(qualifier.get('value'))
                        tempEvent._addQualifier(tempQ)
                events.append(tempEvent)
        return events

    ###########################################
    ## Helper functions for public functions ##
    ###########################################


    ###########################################
    ## Functions for element checking        ##
    ###########################################

    def __loadXMLFile(self):
        "Loads the XML File into Element Tree"
        self.root = ET.parse(self.path).getroot()

    def __checkXMLFile(self):
        "Checks if the XML file is correctly formatted"
        print(Fore.WHITE + " Chekking Games:", end='')
        self.__checkGamesTag()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking Game:", end='')
        self.__checkGameTag()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking Events:", end='')
        self.__checkEventTags()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking Qualifiers:", end='')
        self.__checkQualifierTags()
        print(Fore.BLUE + " OK")

    def __checkGamesTag(self):
        if(self.root.tag != 'Games'):
            print(Fore.RED + "The root tag is not Games!")
            exit()
        if(self.root.get('timestamp') == None):
            print(Fore.RED + "The Games tag has no timestamp!")
            exit()

    def __checkGameTag(self):
        if self.root.find('Game') == None:
            print(Fore.RED + "There is no Game tag!")
            exit()
        if self.root.find('Game').get('away_team_id') == None:
            print(Fore.RED + "There is no away team Id!")
            exit()
        if self.root.find('Game').get('away_team_name') == None:
            print(Fore.RED + "There is no away team name!")
            exit()
        if self.root.find('Game').get('home_team_id') == None:
            print(Fore.RED + "There is no home team Id!")
            exit()
        if self.root.find('Game').get('home_team_name') == None:
            print(Fore.RED + "There is no home team name!")
            exit()
        if self.match.findTeamById('t' + self.root.find('Game').get('home_team_id')) == None:
            print(Fore.RED + "The home team id does not match one of the teams in the match data file!")
            exit()
        if self.match.findTeamById('t' + self.root.find('Game').get('away_team_id')) == None:
            print(Fore.RED + "The away team id does not match one of the teams in the match data file!")
            exit()

    def __checkEventTags(self):
        for game in self.root.iterfind('Game'):
            for event in game.iterfind('Event'):
                if event.get('id') is None:
                    print(Fore.RED + "There is an event without an ID!")
                    exit()
                if event.get('event_id') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute event_id!")
                    exit()
                if event.get('type_id') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute type_id!")
                    exit()
                if event.get('period_id') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute period_id!")
                    exit()
                if event.get('min') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute min!")
                    exit()
                if event.get('sec') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute sec!")
                    exit()
                if event.get('team_id') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute team_id!")
                    exit()
                if event.get('outcome') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute outcome!")
                    exit()
                if event.get('x') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute x!")
                    exit()
                if event.get('y') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute y!")
                    exit()
                if event.get('timestamp') is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has no attribute timestamp!")
                    exit()
                if self.match.findTeamById('t' + event.get('team_id')) is None:
                    print(Fore.RED + "Event with id " + event.get('id') + " has a non existing team ID!")
                    exit()
                if event.get('player_id') is not None:
                    if self.match.findPlayerById('p' + event.get('player_id')) is None:
                        print(Fore.RED + "Event with id " + event.get('id') + " references a non existing player!")
                        exit()

    def __checkQualifierTags(self):
        for game in self.root.iterfind('Game'):
            for event in game.iterfind('Event'):
                if event.find('Q') is not None:
                    for qualifier in event.iterfind('Q'):
                        if qualifier.get('id') is None:
                            print(Fore.RED + "Event with id " + event.get('id') + " has a qualifier without an id!")
                            exit()
                        if qualifier.get('qualifier_id') is None:
                            print(Fore.RED + "Event with id " + event.get('id') + " with qualifier " + qualifier.get('id') + " has no qualifier_id!")
                            exit()