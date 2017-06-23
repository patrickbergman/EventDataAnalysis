import os

from core.classes.Match import Match
from core.colorama import init, Fore
from core.menus.MainMenu import MainMenu
from core.menus.XMLImportMenu import XMLImportMenu
from stats.Passes import printListPlayerPassers
from stats.Passes import printTopPassers
from stats.Passes import printTotalTeamPasses
from stats.TestFunctions import printAllPlayers
from stats.TestFunctions import printAllTeams

init()

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
    if choice == 'z' or choice == 'Z':
        os.system('cls' if os.name == 'nt' else 'clear')
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