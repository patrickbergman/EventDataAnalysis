import os

from core.classes.Match import Match
from core.colorama import init, Fore
from core.menus.MainMenu import MainMenu
from core.menus.XMLImportMenu import XMLImportMenu

from stats.Passes import printListPlayerPassers
from stats.Passes import printTopPassers
from stats.Passes import printTotalTeamPasses
from stats.Passes import printTeamPassesTimeline
from stats.Passes import getAnglesForPasses

from stats.Angles import plotAngles

from stats.TestFunctions import printAllPlayers
from stats.TestFunctions import printAllTeams
from stats.TestFunctions import printSingleTeam
from stats.TestFunctions import printOpposingTeams

from stats.BallPossession import percentagePossession
from stats.BallPossession import intervalPossession
from stats.BallPossession import bestPlayerPossession
from stats.BallPossession import zonePossession
from stats.BallPossession import createDataframe
from stats.BallPossession import histogramPossession

from stats.Duels import printDuelsTimeline

from stats.Throwins import printThrowins

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
        if program.multiple:
            if choice == 'a':
                os.system('cls' if os.name == 'nt' else 'clear')
                printSingleTeam(match)
            if choice == 'b':
                os.system('cls' if os.name == 'nt' else 'clear')
                printOpposingTeams(match)
        else:
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
                printTeamPassesTimeline(match)
            if choice == 'e':
                os.system('cls' if os.name == 'nt' else 'clear')
                printTopPassers(match)
            if choice == 'f':
                os.system('cls' if os.name == 'nt' else 'clear')
                printListPlayerPassers(match)
            if choice == 'g':
                os.system('cls' if os.name == 'nt' else 'clear')
                plotAngles(match)
            if choice == 'h':
                os.system('cls' if os.name == 'nt' else 'clear')
                percentagePossession(match, dataframe, teamComposition)
            if choice == 'i':
                os.system('cls' if os.name == 'nt' else 'clear')
                intervalPossession(match, dataframe, teamComposition)
            if choice == 'j':
                os.system('cls' if os.name == 'nt' else 'clear')
                zonePossession(match, dataframe, teamComposition)
            if choice == 'k':
                os.system('cls' if os.name == 'nt' else 'clear')
                bestPlayerPossession(match, dataframe, teamComposition)
            if choice == 'l':
                os.system('cls' if os.name == 'nt' else 'clear')
                histogramPossession(match, dataframe, teamComposition)
            if choice == 'm':
                os.system('cls' if os.name == 'nt' else 'clear')
                dataframe, teamComposition = createDataframe(match)
            if choice == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                printDuelsTimeline(match)
            if choice == 'o':
                os.system('cls' if os.name == 'nt' else 'clear')
                printThrowins(match)
    else:
        if choice == '1':
            match = xmlMenu.run(match)
            program.xml_is_imported = True
        if choice == '2':
            xmlMenu.multiple = True
            program.multiple = True
            match = xmlMenu.run(match)
            program.xml_is_imported = True    