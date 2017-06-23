import xml.etree.ElementTree as ET

from core.classes.Team import Team
from core.classes.Player import Player
from core.colorama import init, Fore

init()

class MatchXMLImporter:

    def __init__(self, path):
        self.path = path
        self.root = ''
        self.__loadXMLFile()
        self.__checkXMLFile()

    ###########################################
    ## functions for returning elements      ##
    ###########################################

    def getTeamElements(self):
        """Returns an array with team objects (classes)"""
        teams = []
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            tempTeam = Team(team.get('uID'))
            tempTeam._setCountry(team.find('Country').text)
            tempTeam._setName(team.find('Name').text)
            for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
                if teamData.get('TeamRef') == tempTeam.getId():
                    tempTeam._setScore(teamData.get('Score'))
                    tempTeam._setSide(teamData.get('Side'))
            teams.append(tempTeam)
        return teams

    def getPlayers(self):
        players = []
        for team in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            for player in team.find('PlayerLineUp').iterfind('MatchPlayer'):
                tempPlayer = Player(team.get('TeamRef'), player.get('PlayerRef'), player.get('Position'), player.get('ShirtNumber'), player.get('Status'))
                if (player.get('Position') == 'Substitute'):
                    tempPlayer._setSubPosition(player.get('SubPosition'))
                tempPlayer = self.__getPlayerData(tempPlayer, team.get('TeamRef'))
                players.append(tempPlayer)
        return players

    ###########################################
    ## Helper functions for public functions ##
    ###########################################

    def __getPlayerData(self, tempPlayer, teamRef):
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if(team.get('uID') == teamRef):
                for player in team.iterfind('Player'):
                    if(player.get('uID') == tempPlayer.getId()):
                        tempPlayer._setFirstName(player.find('PersonName').find('First').text)
                        tempPlayer._setLastName(player.find('PersonName').find('Last').text)
                        if(player.find('PersonName').find('Known') != None):
                            tempPlayer._setKnownName(player.find('PersonName').find('Known').text)
                        break
        return tempPlayer

    ###########################################
    ## Functions for element checking        ##
    ###########################################

    def __loadXMLFile(self):
        " Loads the XML File into Element Tree "
        self.root = ET.parse(self.path).getroot()

    def __checkXMLFile(self):
        " Checks if the XML file is correctly formatted "
        print(Fore.WHITE + " Chekking SoccerDocument:", end='')
        self.__checkSoccerDocumentExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking MatchData:", end='')
        self.__checkMatchDataExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking Teams:", end='')
        self.__checkTeamExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking TeamData:", end='')
        self.__checkTeamDataExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking Players:", end='')
        self.__checkPlayersExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking PlayerLineUp:", end='')
        self.__checkPlayerLineUpExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking MatchPlayers:", end='')
        self.__checkMatchPlayerExists()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking TeamCountry:", end='')
        self.__checkTeamsHaveCountry()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking TeamName:", end='')
        self.__checkTeamsHaveName()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking TeamID:", end='')
        self.__checkTeamsHaveId()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking all players:", end='')
        self.__checkAllPlayersAndValues()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE + " Chekking all match players:", end='')
        self.__checkMatchPlayerAttributes()
        print(Fore.BLUE + " OK")
        print(Fore.WHITE)

    def __checkSoccerDocumentExists(self):
        if self.root.find('SoccerDocument') == None:
            print(Fore.RED + "The match data XML has not the right content!")
            exit()

    def __checkMatchDataExists(self):
        self.__checkSoccerDocumentExists()
        if self.root.find('SoccerDocument').find('MatchData') == None:
            print(Fore.RED + "Match data does not exists in this file!")
            exit()

    def __checkTeamExists(self):
        self.__checkSoccerDocumentExists()
        if self.root.find('SoccerDocument').find('Team') == None:
            print(Fore.RED + "There are no teams in this file!")
            exit()

    def __checkTeamDataExists(self):
        self.__checkMatchDataExists()
        if self.root.find('SoccerDocument').find('MatchData').find('TeamData') == None:
            print(Fore.RED + "There is no team data available in this file!")
            exit()

    def __checkPlayersExists(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.find('Player') == None:
                print(Fore.RED + "There is a team without players in this file!")
                exit()

    def __checkPlayerLineUpExists(self):
        self.__checkTeamDataExists()
        for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            if teamData.find('PlayerLineUp') == None:
                print(Fore.RED + "There is no player line up for a team!")
                exit()

    def __checkMatchPlayerExists(self):
        self.__checkPlayerLineUpExists()
        for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            if teamData.find('PlayerLineUp').find('MatchPlayer') == None:
                print(Fore.RED + "There is a team without match players!")
                exit()

    def __checkTeamsHaveCountry(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.find('Country') == None:
                print(Fore.RED + "There is a team without a country!")
                exit()

    def __checkTeamsHaveName(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.find('Name') == None:
                print(Fore.RED + "There is a team without a name!")
                exit()

    def __checkTeamsHaveId(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.get('uID') == None:
                print(Fore.RED + "There is a team without an ID!")
                exit()

    def __checkAllPlayersAndValues(self):
        self.__checkPlayersExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            for player in team.iterfind('Player'):
                # check id
                if player.get('uID') == None:
                    print(Fore.RED + "There is a player without an ID!")
                    exit()
                # check Position
                if player.get('Position') == None:
                    print(Fore.RED + "There is a player without a position!")
                    exit()
                # Check if first name exists
                if player.find('PersonName').find('First') == None:
                    print(Fore.RED + "There is a player without a position!")
                    exit()
                # Check if last name exists
                if player.find('PersonName').find('Last') == None:
                    print(Fore.RED + "There is a player without a position!")
                    exit()

    def __checkMatchPlayerAttributes(self):
        self.__checkMatchPlayerExists()
        for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            for matchPlayer in teamData.find('PlayerLineUp').iterfind('MatchPlayer'):
                # check player ref (ID)
                if matchPlayer.get('PlayerRef') == None:
                    print(Fore.RED + "There is a match player without a player reference (ID)!")
                    exit()
                # check position
                if matchPlayer.get('Position') == None:
                    print(Fore.RED + "There is a match player without a player reference (ID)!")
                    exit()
                # check ShirtNumber
                if matchPlayer.get('ShirtNumber') == None:
                    print(Fore.RED + "There is a match player without a shirt number!")
                    exit()
                # check Status
                if matchPlayer.get('Status') == None:
                    print(Fore.RED + "There is a match player without a status!")
                    exit()