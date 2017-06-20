from helpers.colors import Colors

def printAllTeams(match):
    print('List of teams in this match:')
    for team in match.getTeams():
        print(Colors.YELLOW, end='')
        print('Teamnaam: ', end='')
        print(Colors.WHITE, end='')
        print(team.getName())

def printAllPlayers(match):
    print('List of players in this match:')
    for player in match.getPlayers():
        print(Colors.YELLOW, end='')
        print('Speler: ', end='')
        print(Colors.WHITE, end='')
        print(player.getFullName() + Colors.BLUE + ' (' + match.findTeamById(player.getTeamId()).getName() + ')' + Colors.WHITE)