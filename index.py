import os
from helpers.colors import Colors

from classes.Match import Match

from menus.MainMenu import MainMenu
from menus.XMLImportMenu import XMLImportMenu

from stats.TestFunctions import printAllTeams
from stats.TestFunctions import printAllPlayers
from stats.Passes import printTotalTeamPasses

TESTING = True

program = MainMenu()
xmlMenu = XMLImportMenu(TESTING)

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
            printAllTeams(match)
        if choice == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            printAllPlayers(match)
        if choice == 'c':
            os.system('cls' if os.name == 'nt' else 'clear')
            printTotalTeamPasses(match)

    else:
        if choice == '1':
            match = xmlMenu.run(match)
            program.xml_is_imported = True