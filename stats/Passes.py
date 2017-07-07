from core.colorama import init, Fore
from math import atan, degrees
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


from core.colorama import init, Fore
import matplotlib.pyplot as plt
import numpy as np

init()


def __swap(array, indexA, indexB):
    temp = array[indexA]
    array[indexA] = array[indexB]
    array[indexB] = temp
    return array


def __sort(playersArray):
    for i in range(1, len(playersArray)):
        j = i
        while j > 0 and playersArray[j - 1][1] < playersArray[j][1]:
            playersArray = __swap(playersArray, j, j - 1)
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
    print("Top passer: " + Fore.LIGHTBLACK_EX + topPasses[0].getFullName() + Fore.CYAN + " (" + playerData[
        0].getPosition() + ") " + Fore.WHITE + " with " + Fore.GREEN + str(
        topPasses[1]) + Fore.WHITE + " passes (" + Fore.GREEN, end='')
    print("%.2f" % round(topPasses[2], 2), end='')
    print(" % " + Fore.WHITE + " successful passes)")
    print("Top success: " + Fore.LIGHTBLACK_EX + topSuccessRate[0].getFullName() + Fore.CYAN + " (" + playerData[
        0].getPosition() + ") " + Fore.WHITE + " with " + Fore.GREEN, end='')
    print("%.2f" % round(topSuccessRate[2], 2), end='')
    print(" % " + Fore.WHITE + "successful passes (passes made: " + Fore.GREEN + str(
        topSuccessRate[1]) + Fore.WHITE + ")")


def __printTeamPassers(playersArray):
    sortedData = __sort(playersArray)
    for playerData in sortedData:
        print(Fore.LIGHTBLACK_EX + playerData[0].getFullName() + Fore.CYAN + " (" + playerData[
            0].getPosition() + ") " + Fore.WHITE + ": ", end='')
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
    teamApasses = []
    teamAsuccess = []
    teamBpasses = []
    teamBsuccess = []
    time = []
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
                print(Fore.WHITE + teamA.getName() + ": " + Fore.BLUE + str(
                    passesTeamA) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamA, 2), end='')
                print(") ", end='')
                print(Fore.WHITE + teamB.getName() + ": " + Fore.BLUE + str(
                    passesTeamB) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamB, 2), end='')
                print(")")
                teamApasses.append(passesTeamA)
                teamAsuccess.append(successfulPassesTeamA)
                teamBpasses.append(passesTeamB)
                teamBsuccess.append(successfulPassesTeamB)
                time.append(timeframeStart)
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
            # adjust team B
            if event.getTeamId() == teamB.getId():
                # adjust total passes and successrate in this timeframe
                if event.getOutcome() == '1':
                    successfulPassesTeamB = successfulPassesTeamB + 1
                passesTeamB = passesTeamB + 1
                successRateTeamB = (successfulPassesTeamB / passesTeamB) * 100
    time.append(timeframeStart)
    teamApasses.append(passesTeamA)
    teamAsuccess.append(successfulPassesTeamA)
    teamBpasses.append(passesTeamB)
    teamBsuccess.append(successfulPassesTeamB)
    print(Fore.YELLOW + str(timeframeStart) + "-" + str(timeframeEnd) + ": ", end='')
    print(Fore.WHITE + teamA.getName() + ": " + Fore.BLUE + str(passesTeamA) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamA, 2), end='')
    print(") ", end='')
    print(Fore.WHITE + teamB.getName() + ": " + Fore.BLUE + str(passesTeamB) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamB, 2), end='')
    print(")")
    time = [x + 2.5 for x in time]

    plt.plot(time, teamApasses, label='Aantal passes', color='#21468B', linewidth=3)
    plt.plot(time, teamAsuccess, label='Succesvolle passes', color='#21468B', linewidth=3, linestyle='dashed')
    plt.fill_between(time, teamApasses, teamAsuccess, alpha=0.5, color='#21468B')
    plt.xlabel('Tijd (minuten)')
    plt.ylabel('Aantal passes')
    plt.legend()
    plt.xticks(np.arange(0, max(time), 10))
    plt.grid()
    plt.title(teamA.getName())
    plt.show()

    plt.plot(time, teamBpasses, label='Aantal passes', color='#AE1C28', linewidth=3)
    plt.plot(time, teamBsuccess, label='Succesvolle passes', color='#AE1C28', linewidth=3, linestyle='dashed')
    plt.fill_between(time, teamBpasses, teamBsuccess, alpha=0.5, color='#AE1C28')
    plt.xlabel('Tijd (minuten)')
    plt.ylabel('Aantal passes')
    plt.legend()
    plt.xticks(np.arange(0, max(time), 10))
    plt.grid()
    plt.title(teamB.getName())
    plt.show()

def __getAngle(xStart, xEnd, yStart, yEnd):
    if (float(xStart) - float(xEnd)) == 0:
        angle = 0
    else:
        angle = degrees(atan((float(yStart) - float(yEnd)) / (float(xStart) - float(xEnd))))
    if yStart >= yEnd and xStart >= xEnd:
        return angle + 180
    if yStart >= yEnd and xStart < xEnd:
        return angle + 90
    if yStart < yEnd and xStart >= xEnd:
        return angle + 270

    return angle


def getAnglesForPasses(match):
    angleCounts = [0, 0, 0, 0, 0, 0, 0, 0]
    for event in match.getEvents():
        if event.hasQualifierByQualifierId(140) and event.hasQualifierByQualifierId(141):
            angle = __getAngle(event.getXCoordinate(), event.findQualifierByQualifierId(140).getValue(), event.getYCoordinate(), event.findQualifierByQualifierId(141).getValue())
            # print(str(angle))
            if angle < 0:
                angle = angle * -1
            if (angle >= 0 and angle < 45) or angle == 360:
                angleCounts[0] = angleCounts[0] + 1
            if angle >= 45 and angle < 90:
                angleCounts[1] = angleCounts[1] + 1
            if angle >= 90 and angle < 135:
                angleCounts[2] = angleCounts[2] + 1
            if angle >= 135 and angle < 180:
                angleCounts[3] = angleCounts[3] + 1
            if angle >= 180 and angle < 225:
                angleCounts[4] = angleCounts[4] + 1
            if angle >= 225 and angle < 270:
                angleCounts[5] = angleCounts[5] + 1
            if angle >= 270 and angle < 315:
                angleCounts[6] = angleCounts[6] + 1
            if angle >= 315 and angle < 360:
                angleCounts[7] = angleCounts[7] + 1

    print(Fore.YELLOW + "0 - 45 degrees: " + Fore.WHITE + str(angleCounts[0]))
    print(Fore.YELLOW + "45 - 90 degrees: " + Fore.WHITE + str(angleCounts[1]))
    print(Fore.YELLOW + "90 - 135 degrees: " + Fore.WHITE + str(angleCounts[2]))
    print(Fore.YELLOW + "135 - 180 degrees: " + Fore.WHITE + str(angleCounts[3]))
    print(Fore.YELLOW + "180 - 225 degrees: " + Fore.WHITE + str(angleCounts[4]))
    print(Fore.YELLOW + "225 - 270 degrees: " + Fore.WHITE + str(angleCounts[5]))
    print(Fore.YELLOW + "270 - 315 degrees: " + Fore.WHITE + str(angleCounts[6]))
    print(Fore.YELLOW + "315 - 360 degrees: " + Fore.WHITE + str(angleCounts[7]))