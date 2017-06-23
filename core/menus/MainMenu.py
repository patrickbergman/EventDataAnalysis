import os


class MainMenu:

    run_program = True
    xml_is_imported = False

    def showMenu(self):
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
        print('| a) List match teams                 |')
        print('| b) List match players               |')
        print('| c) Teams total passes               |')
        print('| d) Top match passers                |')
        print('| e) List player passes stats         |')
        print('| f) Ball possession in %             |')
        print('| g) Ball possession per interval     |')
        print('| h) Timeline of ball possession      |')
        print('|                                     |')
        print('| Z) Clear screen                     |')
        print('| X) Exit program                     |')

    def __showImportMenu(self):
        print('| 1) Import event and match XML       |')
        print('|                                     |')
        print('| Z) Clear screen                     |')
        print('| X) Exit program                     |')

    def __showMakerText(self):
        print('+--------------------------------------------------------------------------+')
        print('| Leiden University - Sport Data Center                                    |')
        print('| Data analysis for the EK Womens Football competition                     |')
        print('+--------------------------------------------------------------------------+\n')