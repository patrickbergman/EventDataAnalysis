import xml.etree.ElementTree as ET
from helpers.colors import Colors
from classes.Team import Team
from classes.Player import Player

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
            tempTeam.setCountry(team.find('Country').text)
            tempTeam.setName(team.find('Name').text)
            for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
                if teamData.get('TeamRef') == tempTeam.getId():
                    tempTeam.setScore(teamData.get('Score'))
                    tempTeam.setSide(teamData.get('Side'))
            teams.append(tempTeam)
        return teams

    def getPlayers(self):
        players = []
        for team in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            for player in team.find('PlayerLineUp').iterfind('Player'):
                tempPlayer = Player(team.get('TeamRef'), player.get('PlayerRef'), player.get('Position'), player.get('ShirtNumber'), player.get('Status'))
                if (player.get('Position') == 'Substitute'):
                    player.setSubPosition(player.get('SubPosition'))
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
                        tempPlayer.setFirstName(player.find('PersonName').find('First').text)
                        tempPlayer.setLastName(player.find('PersonName').find('Last').text)
                        if(player.find('PersonName').find('Known') != None):
                            tempPlayer.setKwownName(player.find('PersonName').find('Known').text)
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
        print(Colors.WHITE + " Chekking SoccerDocument:", end='')
        self.__checkSoccerDocumentExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking MatchData:", end='')
        self.__checkMatchDataExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking Teams:", end='')
        self.__checkTeamExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking TeamData:", end='')
        self.__checkTeamDataExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking Players:", end='')
        self.__checkPlayersExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking PlayerLineUp:", end='')
        self.__checkPlayerLineUpExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking MatchPlayers:", end='')
        self.__checkMatchPlayerExists()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking TeamCountry:", end='')
        self.__checkTeamsHaveCountry()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking TeamName:", end='')
        self.__checkTeamsHaveName()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking TeamID:", end='')
        self.__checkTeamsHaveId()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking all players:", end='')
        self.__checkAllPlayersAndValues()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE + " Chekking all match players:", end='')
        self.__checkMatchPlayerAttributes()
        print(Colors.BLUE + " OK")
        print(Colors.WHITE)

    def __checkSoccerDocumentExists(self):
        if self.root.find('SoccerDocument') == None:
            print(Colors.RED + "The match data XML has not the right content!")
            exit()

    def __checkMatchDataExists(self):
        self.__checkSoccerDocumentExists()
        if self.root.find('SoccerDocument').find('MatchData') == None:
            print(Colors.RED + "Match data does not exists in this file!")
            exit()

    def __checkTeamExists(self):
        self.__checkSoccerDocumentExists()
        if self.root.find('SoccerDocument').find('Team') == None:
            print(Colors.RED + "There are no teams in this file!")
            exit()

    def __checkTeamDataExists(self):
        self.__checkMatchDataExists()
        if self.root.find('SoccerDocument').find('MatchData').find('TeamData') == None:
            print(Colors.RED + "There is no team data available in this file!")
            exit()

    def __checkPlayersExists(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.find('Player') == None:
                print(Colors.RED + "There is a team without players in this file!")
                exit()

    def __checkPlayerLineUpExists(self):
        self.__checkTeamDataExists()
        for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            if teamData.find('PlayerLineUp') == None:
                print(Colors.RED + "There is no player line up for a team!")
                exit()

    def __checkMatchPlayerExists(self):
        self.__checkPlayerLineUpExists()
        for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            if teamData.find('PlayerLineUp').find('MatchPlayer') == None:
                print(Colors.RED + "There is a team without match players!")
                exit()

    def __checkTeamsHaveCountry(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.find('Country') == None:
                print(Colors.RED + "There is a team without a country!")
                exit()

    def __checkTeamsHaveName(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.find('Name') == None:
                print(Colors.RED + "There is a team without a name!")
                exit()

    def __checkTeamsHaveId(self):
        self.__checkTeamExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            if team.get('uID') == None:
                print(Colors.RED + "There is a team without an ID!")
                exit()

    def __checkAllPlayersAndValues(self):
        self.__checkPlayersExists()
        for team in self.root.find('SoccerDocument').iterfind('Team'):
            for player in team.iterfind('Player'):
                # check id
                if player.get('uID') == None:
                    print(Colors.RED + "There is a player without an ID!")
                    exit()
                # check Position
                if player.get('Position') == None:
                    print(Colors.RED + "There is a player without a position!")
                    exit()
                # Check if first name exists
                if player.find('PersonName').find('First') == None:
                    print(Colors.RED + "There is a player without a position!")
                    exit()
                # Check if last name exists
                if player.find('PersonName').find('Last') == None:
                    print(Colors.RED + "There is a player without a position!")
                    exit()

    def __checkMatchPlayerAttributes(self):
        self.__checkMatchPlayerExists()
        for teamData in self.root.find('SoccerDocument').find('MatchData').iterfind('TeamData'):
            for matchPlayer in teamData.find('PlayerLineUp').iterfind('MatchPlayer'):
                # check player ref (ID)
                if matchPlayer.get('PlayerRef') == None:
                    print(Colors.RED + "There is a match player without a player reference (ID)!")
                    exit()
                # check position
                if matchPlayer.get('Position') == None:
                    print(Colors.RED + "There is a match player without a player reference (ID)!")
                    exit()
                # check ShirtNumber
                if matchPlayer.get('ShirtNumber') == None:
                    print(Colors.RED + "There is a match player without a shirt number!")
                    exit()
                # check Status
                if matchPlayer.get('Status') == None:
                    print(Colors.RED + "There is a match player without a status!")
                    exit()