import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def printDuels(match):
    a = match.getTeams()[0].getId()
    b = match.getTeams()[1].getId()
    groundA, groundB, airA, airB, playersA, playersB = getDuelStats(match, a, b)
    percGroundWonA = (groundA[1] / (groundA[0] + groundA[1])) * 100
    percGroundLostA = (groundA[0] / (groundA[0] + groundA[1])) * 100
    percGroundWonB = (groundB[1] / (groundB[0] + groundB[1])) * 100
    percGroundLostB = (groundB[0] / (groundB[0] + groundB[1])) * 100
    percAirWonA = (airA[1] / (airA[0] + airA[1])) * 100
    percAirLostA = (airA[0] / (airA[0] + airA[1])) * 100
    percAirWonB = (airB[1] / (airB[0] + airB[1])) * 100
    percAirLostB = (airB[0] / (airB[0] + airB[1])) * 100
    print(match.getTeams()[0].getName() + " won " + str(percGroundWonA) + "% of ground duels,\n" +
          match.getTeams()[1].getName() + " won " + str(percGroundWonB) + "% of ground duels.\n")
    print(match.getTeams()[0].getName() + " won " + str(percAirWonA) + "% of aerial duels,\n" +
          match.getTeams()[1].getName() + " won " + str(percAirWonB) + "% of aerial duels.\n")

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
    sizesGround = [percGroundWonA, percGroundWonB]
    sizesAir = [percAirWonA, percAirWonB]
    fig1, (ax1, ax2) = plt.subplots(1, 2)
    fig1.set_size_inches(5, 5)
    patches, texts, autotexts = ax1.pie(sizesGround, autopct='%1.1f%%', startangle=90, colors=['#21468B', '#AE1C28'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Grond", y=0.75, fontsize=10)
    autotexts[0].set_fontsize(10)
    autotexts[1].set_fontsize(10)
    autotexts[0].set_color('white')
    autotexts[1].set_color('white')

    patches, texts, autotexts = ax2.pie(sizesAir, autopct='%1.1f%%', startangle=90, colors=['#21468B', '#AE1C28'])
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title("Lucht", y=0.75, fontsize=10)
    autotexts[0].set_fontsize(10)
    autotexts[1].set_fontsize(10)
    autotexts[0].set_color('white')
    autotexts[1].set_color('white')
    # text = "Team " + match.getTeams()[0].getName() + "\nMost duels: " + match.findPlayerById(
    #    topDuelsA[0]).getFullName() + " with " + str(topDuelsA[1]) + " duels (wins " + str(topDuelsA[2]) + "%)"
    # text += "\nBest dueler: " + match.findPlayerById(topSuccessA[0]).getFullName() + " with " + str(
    #    topSuccessA[2]) + "% of duels won (" + str(topSuccessA[3]) + " out of " + str(topSuccessA[1]) + ")"
    # text += "\nTeam " + match.getTeams()[1].getName() + "\nMost duels: " + match.findPlayerById(
    #    topDuelsB[0]).getFullName() + " with " + str(topDuelsB[1]) + " duels (wins " + str(topDuelsB[2]) + "%)"
    # text += "\nBest dueler: " + match.findPlayerById(topSuccessB[0]).getFullName() + " with " + str(
    #    topSuccessB[2]) + "% of duels won (" + str(topSuccessB[3]) + " out of " + str(topSuccessB[1]) + ")"
    # ax1.text(x=-1.7, y=-1.5, s=text)
    plt.savefig('duels.pdf')
    plt.show()


def getDuelStats(match, a, b):
    events = match.getEvents()
    # duels[0] is #lost, duels[1] is #won
    groundA = [0, 0]
    groundB = [0, 0]
    airA = [0, 0]
    airB = [0, 0]
    # 0 is lost, 1 is won, 2 is total, 3 is percentage
    playersA = {}
    playersB = {}
    for event in events:
        typeId = event.getTypeId()
        teamId = event.getTeamId()
        outcome = event.getOutcome()
        if typeId == "3":
            if teamId == a and outcome == "0":
                groundA[0] += 1
                groundB[1] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][0] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                    playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b and outcome == "1":
                groundA[0] += 1
                groundB[1] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][1] += 1
                playersB[event.getPlayerId()][2] += 1
                playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                    playersB[event.getPlayerId()][2]) * 100 if \
                    playersB[event.getPlayerId()][2] != 0 else 0
            elif teamId == a and outcome == "1":
                groundB[0] += 1
                groundA[1] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][1] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                    playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b and outcome == "0":
                groundB[0] += 1
                groundA[1] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][0] += 1
                playersB[event.getPlayerId()][2] += 1
                playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                    playersB[event.getPlayerId()][2]) * 100 if \
                    playersB[event.getPlayerId()][2] != 0 else 0
        elif typeId == "7":
            if teamId == a:
                groundA[1] += 1
                groundB[0] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][1] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                    playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b:
                groundB[1] += 1
                groundA[0] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][1] += 1
                playersB[event.getPlayerId()][2] += 1
                if playersB[event.getPlayerId()][2] != 0:
                    playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                        playersB[event.getPlayerId()][2]) * 100
        elif typeId == "44":
            if teamId == a:
                airA[int(outcome)] += 1
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
                airB[int(outcome)] += 1
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
                groundA[1] += 1
                groundB[0] += 1
                playersA.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersA[event.getPlayerId()][1] += 1
                playersA[event.getPlayerId()][2] += 1
                playersA[event.getPlayerId()][3] = (playersA[event.getPlayerId()][1] /
                                                    playersA[event.getPlayerId()][2]) * 100 if \
                    playersA[event.getPlayerId()][2] != 0 else 0
            elif teamId == b:
                groundB[1] += 1
                groundA[0] += 1
                playersB.setdefault(event.getPlayerId(), [0, 0, 0, 0])
                playersB[event.getPlayerId()][1] += 1
                playersB[event.getPlayerId()][2] += 1
                playersB[event.getPlayerId()][3] = (playersB[event.getPlayerId()][1] /
                                                    playersB[event.getPlayerId()][2]) * 100 if \
                    playersB[event.getPlayerId()][2] != 0 else 0
    print(groundA, groundB, airA, airB, playersA, playersB)
    return groundA, groundB, airA, airB, playersA, playersB


def getDuelStatsTimeline(match, a, b):
    events = match.getEvents()
    # duels[0] is #lost, duels[1] is #won
    groundAwonTotal = []
    groundBwonTotal = []
    airAwonTotal = []
    airBwonTotal = []
    time = []
    groundAwon = 0
    groundBwon = 0
    airAwon = 0
    airBwon = 0
    timeInterval = 10
    timeframeStart = 0
    timeframeEnd = 10
    for event in events:
        typeId = event.getTypeId()
        teamId = event.getTeamId()
        outcome = event.getOutcome()
        if event.getMinute() >= timeframeEnd and event.getMinute() > 0:
            time.append(timeframeStart)
            groundAwonTotal.append(groundAwon)
            groundBwonTotal.append(groundBwon)
            airAwonTotal.append(airAwon)
            airBwonTotal.append(airBwon)
            timeframeStart = timeframeStart + timeInterval
            timeframeEnd = timeframeEnd + timeInterval
            groundAwon = 0
            groundBwon = 0
            airAwon = 0
            airBwon = 0
        if typeId == "3":
            if teamId == a and outcome == "0":
                groundBwon += 1
            elif teamId == b and outcome == "1":
                groundBwon += 1
            elif teamId == a and outcome == "1":
                groundAwon += 1
            elif teamId == b and outcome == "0":
                groundAwon += 1
        elif typeId == "7":
            if teamId == a:
                groundAwon += 1
            elif teamId == b:
                groundBwon += 1
        elif typeId == "44":
            if teamId == a and outcome == "0":
                airBwon += 1
            elif teamId == b and outcome == "0":
                airAwon += 1
        elif typeId == "54":
            if teamId == a and outcome == "0":
                groundBwon += 1
            elif teamId == b and outcome == "1":
                groundBwon += 1
            elif teamId == a and outcome == "1":
                groundAwon += 1
            elif teamId == b and outcome == "0":
                groundAwon += 1
    time.append(timeframeStart)
    groundAwonTotal.append(groundAwon)
    groundBwonTotal.append(groundBwon)
    airAwonTotal.append(airAwon)
    airBwonTotal.append(airBwon)
    return groundAwonTotal, groundBwonTotal, airAwonTotal, airBwonTotal, time, timeInterval


def printDuelsTimeline(match):
    a = match.getTeams()[0].getId()
    b = match.getTeams()[1].getId()
    groundA, groundB, airA, airB, time, timeInterval = getDuelStatsTimeline(match, a, b)

    groundRange = range(0, ((max(groundA) + max(groundB)) + 1), 2)
    airRange = range(0, ((max(airA) + max(airB)) + 1), 1)
    yticks = []
    for times in time:
        yticks.append(str(times) + ' - ' + str(times + timeInterval))
    time = np.array(time)
    width = 4

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    matplotlib.rcParams.update({'font.size': 26})
    ax1.barh(time, airA, width, label='Gewonnen', color='#21468B')
    ax1.barh(time, airB, width, left=airA, label='Verloren', color='#21468B', alpha=0.5)
    ax1.set_xticks(airRange)
    ax1.set_title('Lucht', y=1.03)
    ax1.set_xlabel('Aantal duels', ha='center', y=0.95)
    ax1.legend()
    ax1.invert_xaxis()
    ax1.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax1.get_yticklabels(), visible=False)

    ax2.barh(time, groundA, width, label='Gewonnen', color='#21468B')
    ax2.barh(time, groundB, width, left=groundA, label='Verloren', color='#21468B', alpha=0.5)
    ax2.set_xticks(groundRange)
    ax2.set_yticks(time)
    ax2.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax2.yaxis.set_label_coords(-0.19, 1.02)
    ax2.set_ylabel('Tijd (min)', ha='center', rotation=0, y=1.03)
    ax2.set_title('Grond', y=1.03)
    ax2.set_xlabel('Aantal duels', ha='center', y=0.95)
    ax2.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax2.get_yticklabels(), visible=True)
    f.subplots_adjust(wspace=0.4)
    plt.show()

    g, (ax3, ax4) = plt.subplots(1, 2, sharey=True)
    ax3.barh(time, airB, width, label='Gewonnen', color='#AE1C28')
    ax3.barh(time, airA, width, left=airB, label='Verloren', color='#AE1C28', alpha=0.5)
    ax3.set_xticks(airRange)
    ax3.set_title('Lucht', y=1.03)
    ax3.set_xlabel('Aantal duels', ha='center', y=0.95)
    ax3.legend()
    ax3.invert_xaxis()
    ax3.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax3.get_yticklabels(), visible=False)

    ax4.barh(time, groundB, width, label='Gewonnen', color='#AE1C28')
    ax4.barh(time, groundA, width, left=groundB, label='Verloren', color='#AE1C28', alpha=0.5)
    ax4.set_xticks(groundRange)
    ax4.set_yticks(time)
    ax4.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax4.yaxis.set_label_coords(-0.19, 1.02)
    ax4.set_ylabel('Tijd (min)', ha='center', rotation=0, y=1.03)
    ax4.set_title('Grond', y=1.03)
    ax4.set_xlabel('Aantal duels', ha='center', y=0.95)
    ax4.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax4.get_yticklabels(), visible=True)
    g.subplots_adjust(wspace=0.4)
    plt.show()
