from helpers.colors import Colors

from classes.Match import Match

from menus.MainMenu import MainMenu
from menus.XMLImportMenu import XMLImportMenu
import os

program = MainMenu()
xmlMenu = XMLImportMenu()

match = Match()

while program.run_program:
    print(Colors.WHITE)
    program.showMenu()
    choice = program.getMenuChoice()

    if choice == 'x' or choice == 'X':
        program.shutDownProgram()
    if program.xml_is_imported:
        if choice == 'a':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('List the teams from the match')
        if choice == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('List the players from the match')
    else:
        if choice == '1':
            match = xmlMenu.run(match)
            program.xml_is_imported = True

# relativeMatchDataPath = input('Please enter the relative path to the match data XML file: ')
# relativeEventDataPath = input('Please enter the relative path to the event data XML file: ')
#
# matchImporter = MatchXMLImporter(relativeMatchDataPath)
# eventImporter = EventXMLImporter(relativeEventDataPath)
#
# create a new match
# match = Match()
#
# Add the teams from the xml to the match
# for team in matchImporter.getTeamElements():
#     match.add_team(team)
#
# print(Colors.WHITE + "Teamnaam: " + match.findTeamById('t6246').getName())