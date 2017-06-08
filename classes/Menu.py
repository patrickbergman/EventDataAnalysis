import os

class Menu:

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

    def __showMainMenu(self):
        print('| 1) Go to Teams menu                 |')
        print('| 2) Go to Players menu               |')
        print('| 3) Go to Events menu                |')

    def __showImportMenu(self):
        print('| 1) Import event and match XML       |')

    def __showMakerText(self):
        print('Data analysis for the EK Womens Football competition')
        print('Written by:')
        print(' - Patrick Bergman')
        print(' - Erik Weenk')
        print('Leiden University - Leiden Sport Data Center')
        print('---------------------------------------------------------------------------------------------------')