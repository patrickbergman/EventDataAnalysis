import os
from colorama import init, Fore

from classes.Match import Match

from menus.MainMenu import MainMenu
from menus.XMLImportMenu import XMLImportMenu

from stats.TestFunctions import printAllTeams
from stats.TestFunctions import printAllPlayers
from stats.Passes import printTotalTeamPasses
from stats.Passes import printTopPassers
from stats.Passes import printListPlayerPassers

TESTING = True

program = MainMenu()
xmlMenu = XMLImportMenu(TESTING)

match = Match()

while program.run_program:
    print(Fore.WHITE)
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
        if choice == 'd':
            os.system('cls' if os.name == 'nt' else 'clear')
            printTopPassers(match)
        if choice == 'e':
            os.system('cls' if os.name == 'nt' else 'clear')
            printListPlayerPassers(match)

    else:
        if choice == '1':
            match = xmlMenu.run(match)
            program.xml_is_imported = True