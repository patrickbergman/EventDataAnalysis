import os
from classes.MatchXMLImporter import MatchXMLImporter


class MainMenu:

    run_program = True
    xml_is_imported = False

    def showMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__showMakerText()
        print('+-------------------------------------+')
        print('| What would you like to do?          |')
        if self.xml_is_imported:
            self.__showMainMenu()
        else:
            self.__showImportMenu()
        print('+-------------------------------------+')

    def getMenuChoice(self):
        choice = input("Your choice: ")
        return choice

    def shutDownProgram(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Thank you for using this program :)')
        self.run_program = False

    def __showMainMenu(self):
        print('| a) Go to Match menu                 |')
        print('| b) Go to Teams menu                 |')
        print('| c) Go to Players menu               |')
        print('| d) Go to Events menu                |')
        print('|                                     |')
        print('| X) Exit program                     |')

    def __showImportMenu(self):
        print('| 1) Import event and match XML       |')
        print('|                                     |')
        print('| X) Exit program                     |')

    def __showMakerText(self):
        print('+--------------------------------------------------------------------------+')
        print('| Leiden University - Sport Data Center                                    |')
        print('| Data analysis for the EK Womens Football competition                     |')
        print('| Written by:                                                              |')
        print('| - Patrick Bergman                                                        |')
        print('| - Erik Weenk                                                             |')
        print('+--------------------------------------------------------------------------+\n')