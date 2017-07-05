import matplotlib.pyplot as plt


def printDuels(match):
    a = match.getTeams()[0].getId()
    b = match.getTeams()[1].getId()
    duelsA, duelsB, playersA, playersB = getDuelStats(match, a, b)
    percWonA = (duelsA[1] / (duelsA[0] + duelsA[1])) * 100
    percLostA = (duelsA[0] / (duelsA[0] + duelsA[1])) * 100
    percWonB = (duelsB[1] / (duelsB[0] + duelsB[1])) * 100
    percLostB = (duelsB[0] / (duelsB[0] + duelsB[1])) * 100
    print(match.getTeams()[0].getName() + " won " + str(percWonA) + "% of the duels,\n" +
          match.getTeams()[1].getName() + " won " + str(percWonB) + "% of the duels.\n")

    # name, total duels, perc win, won duels
    topDuelsA = ['', 0, 0, 0]
    topSuccessA = ['', 0, 0, 0]
    for player, stats in playersA.items():
        if stats[2] > topDuelsA[1]:
            topDuelsA = [player, stats[2], stats[3], stats[1]]
        if stats[3] > topSuccessA[2] or (stats[3] == topSuccessA[2] and stats[2] > topSuccessA[1]):
            topSuccessA = [player, stats[2], stats[3], stats[1]]
    topDuelsB = ['', 0, 0]
    topSuccessB = ['', 0, 0]
    for player, stats in playersB.items():
        if stats[2] > topDuelsB[1]:
            topDuelsB = [player, stats[2], stats[3], stats[1]]
        if stats[3] > topSuccessB[2] or (stats[3] == topSuccessB[2] and stats[2] > topSuccessB[1]):
            topSuccessB = [player, stats[2], stats[3], stats[1]]

    print("Team " + match.getTeams()[0].getName())
    print("Most duels: " + match.findPlayerById(topDuelsA[0]).getFullName() + " with " + str(
        topDuelsA[1]) + " duels (wins " + str(topDuelsA[2]) + "%)")
    print("Best dueler: " + match.findPlayerById(topSuccessA[0]).getFullName() + " with " + str(
        topSuccessA[2]) + "% duels won (" + str(topSuccessA[3]) + " out of " + str(topSuccessA[1]) + ")")
    print("Team " + match.getTeams()[1].getName())
    print("Most duels: " + match.findPlayerById(topDuelsB[0]).getFullName() + " with " + str(
        topDuelsB[1]) + " duels (wins " + str(topDuelsB[2]) + "%)")
    print("Best dueler: " + match.findPlayerById(topSuccessB[0]).getFullName() + " with " + str(
        topSuccessB[2]) + "% duels won (" + str(topSuccessB[3]) + " out of " + str(topSuccessB[1]) + ")")
    labels = match.getTeams()[0].getName(), match.getTeams()[1].getName()
    sizes = [percWonA, percWonB]
    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(7, 5)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    text = "Team " + match.getTeams()[0].getName() + "\nMost duels: " + match.findPlayerById(
        topDuelsA[0]).getFullName() + " with " + str(topDuelsA[1]) + " duels (wins " + str(topDuelsA[2]) + "%)"
    text += "\nBest dueler: " + match.findPlayerById(topSuccessA[0]).getFullName() + " with " + str(
        topSuccessA[2]) + "% of duels won (" + str(topSuccessA[3]) + " out of " + str(topSuccessA[1]) + ")"
    text += "\nTeam " + match.getTeams()[1].getName() + "\nMost duels: " + match.findPlayerById(
        topDuelsB[0]).getFullName() + " with " + str(topDuelsB[1]) + " duels (wins " + str(topDuelsB[2]) + "%)"
    text += "\nBest dueler: " + match.findPlayerById(topSuccessB[0]).getFullName() + " with " + str(
        topSuccessB[2]) + "% of duels won (" + str(topSuccessB[3]) + " out of " + str(topSuccessB[1]) + ")"
    ax1.text(x=-1.7, y=-1.5, s=text)
    plt.title('Duel wins')
    plt.show()


def getDuelStats(match, a, b):
    events = match.getEvents()
    # duels[0] is #lost, duels[1] is #won
    duelsA = [0, 0]
    duelsB = [0, 0]
    # 0 is lost, 1 is won, 2 is total, 3 is percentage
    playersA = {}
    playersB = {}
    for event in events:
        typeId = event.getTypeId()
        teamId = event.getTeamId()
        outcome = event.getOutcome()
        if typeId == "3":
            if teamId == a and outcome == "0":
                duelsA[0] += 1
                duelsB[1] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][0] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b and outcome == "1":
                duelsA[0] += 1
                duelsB[1] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][1] += 1
                playersB[event.getPlayerId()][2] += 1
                playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                    playersB[event.getPlayerId()][2]) * 100 if \
                playersB[event.getPlayerId()][2] != 0 else 0
            elif teamId == a and outcome == "1":
                duelsB[0] += 1
                duelsA[1] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][1] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b and outcome == "0":
                duelsB[0] += 1
                duelsA[1] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][0] += 1
                playersB[event.getPlayerId()][2] += 1
                playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                    playersB[event.getPlayerId()][2]) * 100 if \
                playersB[event.getPlayerId()][2] != 0 else 0
        elif typeId == "7":
            if teamId == a:
                duelsA[1] += 1
                duelsB[0] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][1] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b:
                duelsB[1] += 1
                duelsA[0] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][1] += 1
                playersB[event.getPlayerId()][2] += 1
                if playersB[event.getPlayerId()][2] != 0:
                    playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                        playersB[event.getPlayerId()][2]) * 100
        elif typeId == "44":
            if teamId == a:
                duelsA[int(outcome)] += 1
                if outcome == "0":
                    playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                    playersA[event.getPlayerId()][0] += 1
                    playersA[event.getPlayerId()][2] += 1
                    playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                        playersA[event.getPlayerId()][2]) * 100 if \
                    playersA[event.getPlayerId()][2] != 0 else 0
                elif outcome == "1":
                    playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                    playersA[event.getPlayerId()][1] += 1
                    playersA[event.getPlayerId()][2] += 1
                    playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                        playersA[event.getPlayerId()][2]) * 100 if \
                    playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b:
                duelsB[int(outcome)] += 1
                if outcome == "0":
                    playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                    playersB[event.getPlayerId()][0] += 1
                    playersB[event.getPlayerId()][2] += 1
                    playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                        playersB[event.getPlayerId()][2]) * 100 if \
                    playersB[event.getPlayerId()][2] != 0 else 0
                elif outcome == "1":
                    playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                    playersB[event.getPlayerId()][1] += 1
                    playersB[event.getPlayerId()][2] += 1
                    playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                        playersB[event.getPlayerId()][2]) * 100 if \
                    playersB[event.getPlayerId()][2] != 0 else 0
        elif typeId == "54":
            if teamId == a:
                duelsA[1] += 1
                duelsB[0] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][1] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b:
                duelsB[1] += 1
                duelsA[0] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][1] += 1
                playersB[event.getPlayerId()][2] += 1
                playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                    playersB[event.getPlayerId()][2]) * 100 if \
                playersB[event.getPlayerId()][2] != 0 else 0
    return duelsA, duelsB, playersA, playersB