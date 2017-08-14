import os


class MainMenu:

    run_program = True
    xml_is_imported = False
    multiple = False

    def showMenu(self):
        self.__showMakerText()
        print('+-------------------------------------+')
        print('| What would you like to do?          |')
        if self.xml_is_imported:
            if self.multiple:
                self.__showMainMenuMultiple()
            else:
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
        print('| i) Ball possession per zone         |')
        print('| j) Player with most ball possession |')
        print('| k) Histogram of ball possession     |')
        print('| l) Create dataframe for possession  |')
        print('|                                     |')
        print('+--------- Duels ---------------------+')
        print('|                                     |')
        print('| m) Plot duels                       |')
        print('| n) Plot aerial duels                |')
        print('|                                     |')
        print('+--------- Throw-ins -----------------+')
        print('|                                     |')
        print('| o) Plot throw-ins                   |')
        print('|                                     |')
        print('+--------- System --------------------+')
        print('|                                     |')
        print('| Z) Clear screen                     |')
        print('| X) Exit program                     |')

    def __showMainMenuMultiple(self):
        print('+--------- General -------------------+')
        print('|                                     |')
        print('| a) Show common team                 |')
        print('| b) Show opposing teams              |')
        print('|                                     |')
        print('+--------- Duels ---------------------+')
        print('|                                     |')
        print('| c) Plot duels                       |')
        print('|                                     |')
        print('+--------- Throwins ------------------+')
        print('|                                     |')
        print('| d) Plot throwins                    |')
        print('|                                     |')
        print('+--------- System --------------------+')
        print('|                                     |')
        print('| Z) Clear screen                     |')
        print('| X) Exit program                     |')

    def __showImportMenu(self):
        print('| 1) Import event and match XML       |')
        print('| 2) Import multiple event and match  |')
        print('|    XML                              |')
        print('|                                     |')
        print('| Z) Clear screen                     |')
        print('| X) Exit program                     |')

    def __showMakerText(self):
        print('+--------------------------------------------------------------------------+')
        print('| Leiden University - Sport Data Center                                    |')
        print('| Data analysis for the EK Womens Football competition                     |')
        print('+--------------------------------------------------------------------------+\n')