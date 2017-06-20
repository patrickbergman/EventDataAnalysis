# About this program

This program is written at the Leiden University for the Leiden Sport Data Center.

It is a tool to analys match data and event data from soccer matches.

## Installation

Required:

Python 3.6

Just download the files and run with:
```
python3 index.py
```

## Adding statistics functions
1) Add a new python file in the folder 'stats' with your functions
2) Import the function in index.py with ``` from stats.FileName import function ```
3) Add your short function description to the menu as a menu option in menus/MainMenu.py inside the function __showMainMenu
4) Add your function in the main loop like the example beneath:
```python
if choice == 'menuOption':
    os.system('cls' if os.name == 'nt' else 'clear')
    yourStatsFunction(match)
```
5) from the 'match' variable you can get all the data you need

## Object functionalities
Beneath you will find the functions a match, team or player has. Although the classes contain more function,
the function prepended with a single underscore (_function) are use by the importer to set data.
The functions prepended with a double underscore (__function) are used by the class itself and are meant to be 'private' functions

The functions with a _ and a __ are not suppost to be used to generate statistics!!
### Match functions
function | output
--- | ---
findTeamById(teamId) | Returns a team object when found (teamId is obligatory)
findPlayerById(playerId) | Returns a player object when found (playerId is obligatory)
getTeams() | Returns an array with all teams (as Team class) of the match
getPlayers() | Returns an array with all match players as Player class

### Team functions
function | output
--- | ---
getId() | Returns the team id as a string
getName() | Returns the team name as a string

### Player functions
function | output
--- | ---
getId() | Returns the player id as a string
getTeamId() | Returns the id of the team to which the player belongs as a string
getFullName() | Returns the full name of a player as a string

### Event functions
None

### Qualifier functions
None

## Contributers
- Patrick Bergman
- Erik Weenk