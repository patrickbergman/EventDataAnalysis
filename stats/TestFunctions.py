from core.colorama import Fore

def printAllTeams(match):
    print('List of teams in this match:')
    for team in match.getTeams():
        print(Fore.YELLOW, end='')
        print('Teamnaam: ', end='')
        print(Fore.WHITE, end='')
        print(team.getName())

def printAllPlayers(match):
    print('List of players in this match:')
    for player in match.getPlayers():
        print(Fore.YELLOW, end='')
        print('Speler: ', end='')
        print(Fore.WHITE, end='')
        print(player.getFullName() + Fore.BLUE + ' (' + match.findTeamById(player.getTeamId()).getName() + ')' + Fore.WHITE)

