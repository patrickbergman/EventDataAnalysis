from core.colorama import init, Fore
init()

def __swap(array, indexA, indexB):
    temp = array[indexA]
    array[indexA] = array[indexB]
    array[indexB] = temp
    return array

def __sort(playersArray):
    for i in range(1, len(playersArray)):
        j = i
        while j > 0 and playersArray[j-1][1] < playersArray[j][1]:
            playersArray = __swap(playersArray, j, j-1)
            j = j - 1

    return playersArray

def __printTeamTopPassers(playersArray):
    topSuccessRate = ['', 0, 0]
    topPasses = ['', 0, 0]
    for playerData in playersArray:
        # print("%.2f" % round(playerData[2], 2))
        if playerData[1] > topPasses[1]:
            topPasses = playerData
        if playerData[2] > topSuccessRate[2]:
            topSuccessRate = playerData
    print("Top passer: " + Fore.LIGHTBLACK_EX + topPasses[0].getFullName() + Fore.CYAN + " (" + playerData[0].getPosition() + ") " + Fore.WHITE + " with " + Fore.GREEN + str(topPasses[1]) + Fore.WHITE + " passes (" + Fore.GREEN, end='')
    print("%.2f" % round(topPasses[2], 2), end='')
    print(" % " + Fore.WHITE + " successful passes)")
    print("Top success: " + Fore.LIGHTBLACK_EX + topSuccessRate[0].getFullName() + Fore.CYAN + " (" + playerData[0].getPosition() + ") " + Fore.WHITE + " with " + Fore.GREEN, end='')
    print("%.2f" % round(topSuccessRate[2], 2), end='')
    print(" % " + Fore.WHITE + "successful passes (passes made: " + Fore.GREEN + str(topSuccessRate[1]) + Fore.WHITE + ")")

def __printTeamPassers(playersArray):
    sortedData = __sort(playersArray)
    for playerData in sortedData:
        print(Fore.LIGHTBLACK_EX + playerData[0].getFullName() + Fore.CYAN + " (" + playerData[0].getPosition() + ") " + Fore.WHITE + ": ", end='')
        print(Fore.GREEN + str(playerData[1]) + Fore.WHITE + " passes (" + Fore.GREEN, end='')
        print("%.2f" % round(playerData[2], 2), end='')
        print(" %" + Fore.WHITE + " successful)")

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

def printListPlayerPassers(match):
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
        __printTeamPassers(teamPlayerPasses)

def printTeamPassesTimeline(match):
    timeframeStart = 0
    timeframeEnd = 5
    teamA = match.getTeams()[0]
    teamB = match.getTeams()[1]
    passesTeamA = 0
    passesTeamB = 0
    successfulPassesTeamA = 0
    successfulPassesTeamB = 0
    successRateTeamA = 0
    successRateTeamB = 0
    for event in match.getEvents():
        # check if the event is a pass
        if event.getTypeId() == '1' or event.getTypeId() == '2':
            # check new timeframe, then print current stats and reset them
            if event.getMinute() >= timeframeEnd and event.getMinute() > 0:
                print(Fore.YELLOW + str(timeframeStart) + "-" + str(timeframeEnd) + ": ", end='')
                print(Fore.WHITE + teamA.getName() + ": " + Fore.BLUE + str(passesTeamA) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamA, 2), end='')
                print(") ", end='')
                print(Fore.WHITE + teamB.getName() + ": " + Fore.BLUE + str(passesTeamB) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamB, 2), end='')
                print(")")
                timeframeStart = timeframeStart + 5
                timeframeEnd = timeframeEnd + 5
                passesTeamA = 0
                passesTeamB = 0
                successfulPassesTeamA = 0
                successfulPassesTeamB = 0
                successRateTeamA = 0
                successRateTeamB = 0
            # adjust team A
            if event.getTeamId() == teamA.getId():
                # adjust total passes and successrate in this timeframe
                if event.getOutcome() == '1':
                    successfulPassesTeamA = successfulPassesTeamA + 1
                passesTeamA = passesTeamA + 1
                successRateTeamA = (successfulPassesTeamA / passesTeamA) * 100
            #adjust team B
            if event.getTeamId() == teamB.getId():
                # adjust total passes and successrate in this timeframe
                if event.getOutcome() == '1':
                    successfulPassesTeamB = successfulPassesTeamB + 1
                passesTeamB = passesTeamB + 1
                successRateTeamB = (successfulPassesTeamB / passesTeamB) * 100
    print(Fore.YELLOW + str(timeframeStart) + "-" + str(timeframeEnd) + ": ", end='')
    print(Fore.WHITE + teamA.getName() + ": " + Fore.BLUE + str(passesTeamA) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamA, 2), end='')
    print(") ", end='')
    print(Fore.WHITE + teamB.getName() + ": " + Fore.BLUE + str(passesTeamB) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamB, 2), end='')
    print(")")



