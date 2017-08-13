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

## Importing multiple matches
To import multiple matches, make sure that every match has its own folder in './data'. 
Each folder needs to contain a 'match.xml' and a 'events.xml'.

## Object functionalities
Beneath you will find the functions a match, team or player has. Although the classes contain more function,
the function prepended with a single underscore (_function) are use by the importer to set data.
The functions prepended with a double underscore (__function) are used by the class itself and are meant to be 'private' functions

The functions with a _ and a __ are not suppost to be used to generate statistics!!
### Match functions
function | output
--- | ---
findTeamById(teamId) | Returns a team object when found
findPlayerById(playerId) | Returns a player object when found
findEventsByQualifierId(qId) | Returns an array with all events that have a qualifier with qId as qualifier_id
getTeams() | Returns an array with all teams (as Team class) of the match
getPlayers() | Returns an array with all match players as Player class
getEvents() | Returns an array with all match events as Event class

### Team functions
function | output
--- | ---
getId() | Returns the team id as a string
getName() | Returns the team name as a string
getEvents() | Returns an array with all match events as Event class
findPlayerById(playerId) | Returns a player object when found
findEventsByQualifierId(qId) | Returns an array with all events that have a qualifier with qId as qualifier_id

### Player functions
function | output
--- | ---
getId() | Returns the player id as a string
getTeamId() | Returns the id of the team to which the player belongs as a string
getFullName() | Returns the full name of a player as a string
getEvents() | Returns an array with all match events as Event class
findEventsByQualifierId(qId) | Returns an array with all events that have a qualifier with qId as qualifier_id

### Event functions
function | output
--- | ---
getId() | Returns a string with the id of the event
getEventId() | Returns a string with the event id
getTypeId() | Returns a string with the type id
getPeriodeId() | Returns a string with the period id
getMinute() | Returns a string with the minute of the match when the event occurs
getSecond() | Returns a string with the second of the match when the event occurs
getTeamId() | Returns a string with the team id
getOutcome() | Returns a string with the outcome
getXCoordinate() | Returns a string with the x coordinate
getYCoordinate() | Returns a string with the Y coordinate
getTimestamp() | Returns a string with the timestamp
hasPlayerId() | Returns a boolean which indicates if the event has a playerId
getPlayerId() | Returns a string with the player id from the event
hasPlayer() | Returns a boolean which indicates if the event has a player class
getPlayer() | Returns a string with the player class belonging to the event
getQualifiers() | Returns an array with all qualifiers belonging to the event
findQualifierByQualifierId(qId) | Returns a qualifier class when found, otherwise None is returned

### Qualifier functions
function | output
--- | ---
getId() | Returns a string with the id of the qualifier
getQualifierId() | Returns a string with the qualifier id
hasValue() | Returns a boolean which indicates if the qualifier has a value
getValue() | Returns a string with the value of the qualifier

## Contributers
- Patrick Bergman
- Erik Weenk
- Lars Suanet
- Jody Liu