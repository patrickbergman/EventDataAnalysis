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
        print('+--------- General -------------------+')
        print('|                                     |')
        print('| a) List match teams                 |')
        print('| b) List match players               |')
        print('|                                     |')
        print('+--------- Passes --------------------+')
        print('|                                     |')
        print('| c) Teams total passes               |')
        print('| d) Teams total passes (timeline)    |')
        print('| e) Top match passers                |')
        print('| f) List player passes stats         |')
        print('| g) Show pass angle stats            |')
        print('|                                     |')
        print('+--------- Ball Posesion -------------+')
        print('|                                     |')
        print('| h) Ball possession in percentage    |')
        print('| i) Ball possession per interval     |')
        print('| j) Ball possession per zone         |')
        print('| k) Player with most ball possession |')
        print('| l) Histogram of ball possession     |')
        print('| m) Create dataframe for possession  |')
        print('|                                     |')
        print('+--------- Duals ---------------------+')
        print('|                                     |')
        print('| n) Plot duals                       |')
        print('|                                     |')
        print('+--------- System --------------------+')
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