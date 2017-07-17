from core.colorama import init, Fore
import matplotlib.pyplot as plt
from math import atan, degrees
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
    teamApassesOwnHalf = []
    teamApassesOpponentHalf = []
    teamAsuccessOwnHalf = []
    teamAsuccessOpponentHalf = []
    teamBpassesOwnHalf = []
    teamBpassesOpponentHalf = []
    teamBsuccessOwnHalf = []
    teamBsuccessOpponentHalf = []
    time = []
    passesTeamAOwnHalf = 0
    passesTeamAOpponentHalf = 0
    passesTeamBOwnHalf = 0
    passesTeamBOpponentHalf = 0
    successfulPassesTeamAOwnHalf = 0
    successfulPassesTeamAOpponentHalf = 0
    successfulPassesTeamBOwnHalf = 0
    successfulPassesTeamBOpponentHalf = 0
    successRateTeamAOwnHalf = 0
    successRateTeamAOpponentHalf = 0
    successRateTeamBOwnHalf = 0
    successRateTeamBOpponentHalf = 0
    for event in match.getEvents():
        # check if the event is a pass
        if (event.getTypeId() == '1' or event.getTypeId() == '2') and not event.hasQualifierByQualifierId(2) and not event.hasQualifierByQualifierId(107) and not event.hasQualifierByQualifierId(123):
            # check new timeframe, then print current stats and reset them
            if event.getMinute() >= timeframeEnd and event.getMinute() > 0:
                print(Fore.YELLOW + str(timeframeStart) + "-" + str(timeframeEnd) + ": ", end='')
                print(Fore.WHITE + teamA.getName() + " Own Half: " + Fore.BLUE + str(
                    passesTeamAOwnHalf) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamAOwnHalf, 2), end='')
                print(") ", end='')
                print(Fore.WHITE + teamA.getName() + " Opponent Half: " + Fore.BLUE + str(
                    passesTeamAOpponentHalf) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamAOpponentHalf, 2), end='')
                print(") ", end='')
                print(Fore.WHITE + teamB.getName() + " Own Half: " + Fore.BLUE + str(
                    passesTeamBOwnHalf) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamBOwnHalf, 2), end='')
                print(")")
                print(Fore.WHITE + teamB.getName() + " Opponent Half: " + Fore.BLUE + str(
                    passesTeamBOpponentHalf) + " passes " + Fore.MAGENTA + "(", end='')
                print("%.2f" % round(successRateTeamBOpponentHalf, 2), end='')
                print(")")
                teamApassesOwnHalf.append(passesTeamAOwnHalf)
                teamApassesOpponentHalf.append(passesTeamAOpponentHalf)
                teamAsuccessOwnHalf.append(successfulPassesTeamAOwnHalf)
                teamAsuccessOpponentHalf.append(successfulPassesTeamAOpponentHalf)
                teamBpassesOwnHalf.append(passesTeamBOwnHalf)
                teamBpassesOpponentHalf.append(passesTeamBOpponentHalf)
                teamBsuccessOwnHalf.append(successfulPassesTeamBOwnHalf)
                teamBsuccessOpponentHalf.append(successfulPassesTeamBOpponentHalf)
                time.append(timeframeStart)
                # Set new timeframe for counting
                timeframeStart = timeframeStart + 5
                timeframeEnd = timeframeEnd + 5
                # Reset Counters
                passesTeamAOwnHalf = 0
                passesTeamAOpponentHalf = 0
                passesTeamBOwnHalf = 0
                passesTeamBOpponentHalf = 0
                successfulPassesTeamAOwnHalf = 0
                successfulPassesTeamAOpponentHalf = 0
                successfulPassesTeamBOwnHalf = 0
                successfulPassesTeamBOpponentHalf = 0
                successRateTeamAOwnHalf = 0
                successRateTeamAOpponentHalf = 0
                successRateTeamBOwnHalf = 0
                successRateTeamBOpponentHalf = 0
            # adjust team A
            if event.getTeamId() == teamA.getId():
                # adjust total passes and successrate in this timeframe
                if float(event.getXCoordinate()) <= 50.0: # own half
                    if event.getOutcome() == '1':
                        successfulPassesTeamAOwnHalf = successfulPassesTeamAOwnHalf + 1
                    passesTeamAOwnHalf = passesTeamAOwnHalf + 1
                    successRateTeamAOwnHalf = (successfulPassesTeamAOwnHalf / passesTeamAOwnHalf) * 100
                else: # opponent half
                    if event.getOutcome() == '1':
                        successfulPassesTeamAOpponentHalf = successfulPassesTeamAOpponentHalf + 1
                    passesTeamAOpponentHalf = passesTeamAOpponentHalf + 1
                    successRateTeamAOpponentHalf = (successfulPassesTeamAOpponentHalf / passesTeamAOpponentHalf) * 100
            # adjust team B
            if event.getTeamId() == teamB.getId():
                # adjust total passes and successrate in this timeframe
                if float(event.getXCoordinate()) <= 50.0: # own half
                    if event.getOutcome() == '1':
                        successfulPassesTeamBOwnHalf = successfulPassesTeamBOwnHalf + 1
                    passesTeamBOwnHalf = passesTeamBOwnHalf + 1
                    successRateTeamBOwnHalf = (successfulPassesTeamBOwnHalf / passesTeamBOwnHalf) * 100
                else: # opponent half
                    if event.getOutcome() == '1':
                        successfulPassesTeamBOpponentHalf = successfulPassesTeamBOpponentHalf + 1
                    passesTeamBOpponentHalf = passesTeamBOpponentHalf + 1
                    successRateTeamBOpponentHalf = (successfulPassesTeamBOpponentHalf / passesTeamBOpponentHalf) * 100
    time.append(timeframeStart)
    teamApassesOwnHalf.append(passesTeamAOwnHalf)
    teamApassesOpponentHalf.append(passesTeamAOpponentHalf)
    teamAsuccessOwnHalf.append(successfulPassesTeamAOwnHalf)
    teamAsuccessOpponentHalf.append(successfulPassesTeamAOpponentHalf)
    teamBpassesOwnHalf.append(passesTeamBOwnHalf)
    teamBpassesOpponentHalf.append(passesTeamBOpponentHalf)
    teamBsuccessOwnHalf.append(successfulPassesTeamBOwnHalf)
    teamBsuccessOpponentHalf.append(successfulPassesTeamBOpponentHalf)
    print(Fore.YELLOW + str(timeframeStart) + "-" + str(timeframeEnd) + ": ", end='')
    print(Fore.WHITE + teamA.getName() + " Own Half: " + Fore.BLUE + str(passesTeamAOwnHalf) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamAOwnHalf, 2), end='')
    print(") ", end='')
    print(Fore.WHITE + teamA.getName() + " Opponent Half: " + Fore.BLUE + str(passesTeamAOpponentHalf) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamAOpponentHalf, 2), end='')
    print(") ", end='')
    print(Fore.WHITE + teamB.getName() + " Own Half: " + Fore.BLUE + str(passesTeamBOwnHalf) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamBOwnHalf, 2), end='')
    print(")")
    print(Fore.WHITE + teamB.getName() + " Opponent Half: " + Fore.BLUE + str(passesTeamBOpponentHalf) + " passes " + Fore.MAGENTA + "(", end='')
    print("%.2f" % round(successRateTeamBOpponentHalf, 2), end='')
    print(")")
    time = [x + 2.5 for x in time]

    plt.plot(time, teamApassesOwnHalf, label='Aantal passes', color='#21468B', linewidth=3)
    plt.plot(time, teamAsuccessOwnHalf, label='Succesvolle passes', color='#21468B', linewidth=3, linestyle='dashed')
    plt.fill_between(time, teamApassesOwnHalf, teamAsuccessOwnHalf, alpha=0.5, color='#21468B')
    plt.xlabel('Tijd (minuten)')
    plt.ylabel('Aantal passes')
    plt.legend()
    plt.xticks(np.arange(0, max(time), 10))
    plt.grid()
    plt.title('Eigen Helft')
    plt.show()

    plt.plot(time, teamApassesOpponentHalf, label='Aantal passes', color='#21468B', linewidth=3)
    plt.plot(time, teamAsuccessOpponentHalf, label='Succesvolle passes', color='#21468B', linewidth=3, linestyle='dashed')
    plt.fill_between(time, teamApassesOpponentHalf, teamAsuccessOpponentHalf, alpha=0.5, color='#21468B')
    plt.xlabel('Tijd (minuten)')
    plt.ylabel('Aantal passes')
    plt.legend()
    plt.xticks(np.arange(0, max(time), 10))
    plt.grid()
    plt.title('Tegenstander Helft')
    plt.show()

    plt.plot(time, teamBpassesOwnHalf, label='Aantal passes', color='#AE1C28', linewidth=3)
    plt.plot(time, teamBsuccessOwnHalf, label='Succesvolle passes', color='#AE1C28', linewidth=3, linestyle='dashed')
    plt.fill_between(time, teamBpassesOwnHalf, teamBsuccessOwnHalf, alpha=0.5, color='#AE1C28')
    plt.xlabel('Tijd (minuten)')
    plt.ylabel('Aantal passes')
    plt.legend()
    plt.xticks(np.arange(0, max(time), 10))
    plt.grid()
    plt.title('Eigen Helft')
    plt.show()

    plt.plot(time, teamBpassesOpponentHalf, label='Aantal passes', color='#AE1C28', linewidth=3)
    plt.plot(time, teamBsuccessOpponentHalf, label='Succesvolle passes', color='#AE1C28', linewidth=3, linestyle='dashed')
    plt.fill_between(time, teamBpassesOpponentHalf, teamBsuccessOpponentHalf, alpha=0.5, color='#AE1C28')
    plt.xlabel('Tijd (minuten)')
    plt.ylabel('Aantal passes')
    plt.legend()
    plt.xticks(np.arange(0, max(time), 10))
    plt.grid()
    plt.title('Tegenstander Helft')
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