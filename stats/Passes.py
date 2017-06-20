from colorama import init, Fore
init()

def __printTeamTopPassers(playersArray):
    topSuccessRate = ['', 0, 0];
    topPasses = ['', 0, 0];
    for playerData in playersArray:
        # print("%.2f" % round(playerData[2], 2))
        if playerData[1] > topPasses[1]:
            topPasses = playerData
        if playerData[2] > topSuccessRate[2]:
            topSuccessRate = playerData
    print("Top passer: " + Fore.GREEN + topPasses[0].getFullName() + Fore.WHITE + " with " + Fore.GREEN + str(topPasses[1]) + Fore.WHITE + " passes (" + Fore.GREEN, end='')
    print("%.2f" % round(topPasses[2], 2), end='')
    print(" % " + Fore.WHITE + " successful passes)")
    print("Top success: " + Fore.GREEN + topSuccessRate[0].getFullName() + Fore.WHITE + " with " + Fore.GREEN, end='')
    print("%.2f" % round(topSuccessRate[2], 2), end='')
    print(" % " + Fore.WHITE + "successful passes (passes made: " + str(topSuccessRate[1]) + ")")

def printTotalTeamPasses(match):
    for team in match.getTeams():
        successFullPasses = 0
        passes = team.getEventsByTypeId(1)
        offsidePasses = team.getEventsByTypeId(2)
        totalPasses = passes + offsidePasses

        for playerPassEvent in totalPasses:
            if playerPassEvent.getOutcome() == '1':
                successFullPasses = successFullPasses + 1
        passesPercentage = (successFullPasses / len(totalPasses)) * 100
        print(Fore.YELLOW, end='')
        print(team.getName(), end='')
        print(Fore.WHITE, end='')
        print(": " + str(len(totalPasses)) + " passes (", end='')
        print("%.2f" % round(passesPercentage, 2), end='')
        print("% successfull)")

def printTopPassers(match):
    for team in match.getTeams():
        teamPlayerPasses = []
        for player in team.getPlayers():
            passes = player.getEventsByTypeId(1)
            offsidePasses = player.getEventsByTypeId(2)
            totalPasses = passes + offsidePasses
            successFullPasses = 0
            for playerPassEvent in totalPasses:
                if playerPassEvent.getOutcome() == '1':
                    successFullPasses = successFullPasses + 1
            successRate = (successFullPasses / len(totalPasses)) * 100 if len(totalPasses) > 0 else 0
            teamPlayerPasses.append([
                player,
                len(totalPasses),
                successRate
            ])
        print(Fore.YELLOW + "Team " + team.getName() + ":" + Fore.WHITE)
        __printTeamTopPassers(teamPlayerPasses)