import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from operator import eq

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
    airRange = range(0, ((max(airA) + max(airB)) + 1), 2)
    yticks = []
    for times in time:
        yticks.append(str(times) + ' - ' + str(times + timeInterval))
    time = np.array(time)
    width = 4

    print(match.getTeams()[0].getName() + "blue")
    print(match.getTeams()[1].getName() + "red")
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    matplotlib.rcParams.update({'font.size': 26})
    ax1.barh(time, airA, width, label='Gewonnen', color='#21468B')
    ax1.barh(time, airB, width, left=airA, label='Verloren', color='#21468B', alpha=0.5)
    ax1.set_xticks(airRange)
#    ax1.set_xticks(range(0,13,2))
    ax1.set_title('Lucht', y=1.03)
    ax1.set_xlabel('Aantal duels', ha='center', y=0.95)
    ax1.legend(loc=2)
    ax1.invert_xaxis()
    ax1.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax1.get_yticklabels(), visible=False)

    ax2.barh(time, groundA, width, label='Gewonnen', color='#21468B')
    ax2.barh(time, groundB, width, left=groundA, label='Verloren', color='#21468B', alpha=0.5)
    ax2.set_xticks(groundRange)
#    ax2.set_xticks(range(0,21,2))
    ax2.set_yticks(time)
    ax2.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax2.yaxis.set_label_coords(-0.19, 1.02)
    ax2.set_ylabel('Tijd (min)', ha='center', rotation=0, y=1.03)
    ax2.set_title('Grond', y=1.03)
    ax2.set_xlabel('Aantal duels', ha='center', y=0.95)
#    ax2.legend(loc = 1)
    ax2.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax2.get_yticklabels(), visible=True)
    f.subplots_adjust(wspace=0.4)
    plt.show()

    g, (ax3, ax4) = plt.subplots(1, 2, sharey=True)
    ax3.barh(time, airB, width, label='Gewonnen', color='#AE1C28')
    ax3.barh(time, airA, width, left=airB, label='Verloren', color='#AE1C28', alpha=0.5)
    ax3.set_xticks(airRange)
#    ax3.set_xticks(range(0,13,2))
    ax3.set_title('Lucht', y=1.03)
    ax3.set_xlabel('Aantal duels', ha='center', y=0.95)
    ax3.legend(loc=2)
    ax3.invert_xaxis()
    ax3.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax3.get_yticklabels(), visible=False)

    ax4.barh(time, groundB, width, label='Gewonnen', color='#AE1C28')
    ax4.barh(time, groundA, width, left=groundB, label='Verloren', color='#AE1C28', alpha=0.5)
    ax4.set_xticks(groundRange)
#    ax4.set_xticks(range(0,21,2))
    ax4.set_yticks(time)
    ax4.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax4.yaxis.set_label_coords(-0.19, 1.02)
    ax4.set_ylabel('Tijd (min)', ha='center', rotation=0, y=1.03)
    ax4.set_title('Grond', y=1.03)
    ax4.set_xlabel('Aantal duels', ha='center', y=0.95)
#    ax4.legend(loc = 1)
    ax4.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax4.get_yticklabels(), visible=True)
    g.subplots_adjust(wspace=0.4)
    plt.show()
    
def getAerialStats(match, a, b):
    events = match.getEvents()
    eventIds = []
    aerialEventId = []
    nextEventId = []
    nextnextEventId = []
    teamId = []
    eventData = []
    teamEventId = []
    minute = []
    time = []
    period = []
    xCoordA = []
    zone1AWon = 0
    zone1BWon = 0
    zone2AWon = 0
    zone2BWon = 0
    zone3AWon = 0
    zone3BWon = 0
    zone4AWon = 0
    zone4BWon = 0
    zone5AWon = 0
    zone5BWon = 0
    zone6AWon = 0
    zone6BWon = 0
    zoneAWon = []
    zoneBWon = []
    wonAerialKeepBallATotalFirst = []
    wonAerialKeepBallATotalSecond = []
    wonAerialKeepBallATotalET = []
    wonAerialKeepBallATotal = []
    wonAerialKeepBallBTotalFirst = []
    wonAerialKeepBallBTotalSecond = []
    wonAerialKeepBallBTotalET = []
    wonAerialKeepBallBTotal = []
    wonAerialLostBallATotalFirst = []
    wonAerialLostBallATotalSecond = []
    wonAerialLostBallATotalET = []
    wonAerialLostBallATotal = []
    wonAerialLostBallBTotalFirst = []
    wonAerialLostBallBTotalSecond = []
    wonAerialLostBallBTotalET = []
    wonAerialLostBallBTotal = []
    wonAerialKeepBallAFirst = 0
    wonAerialKeepBallASecond = 0
    wonAerialKeepBallAET = 0
    wonAerialKeepBallBFirst = 0
    wonAerialKeepBallBSecond = 0
    wonAerialKeepBallBET = 0
    wonAerialLostBallAFirst = 0
    wonAerialLostBallASecond = 0
    wonAerialLostBallAET = 0
    wonAerialLostBallBFirst = 0
    wonAerialLostBallBSecond = 0
    wonAerialLostBallBET = 0
    timeInterval = 10
    timeframeStart = 0
    timeframeEnd = timeInterval
    for event in events:
        typeId = event.getTypeId()   
        outcome = event.getOutcome()
        if typeId != "43": #als een event geen verwijderde event is
            eventIds.append(event.getId()) #voeg de ID toe aan de lijst met eventsIds
        if typeId == "44": 
            aerialEventId.append(event.getId()) #alle aerial events verzamelen
            if outcome == "1": 
                teamId.append(event.getTeamId()) #team dat duel wint aan lijst toevoegen
                eventData.append((event.getPlayerId(), event.getId(), event.getPeriodId()))
            if event.getTeamId() == a:
                xCoordA.append(event.getXCoordinate())
    eventId = iter(eventIds)
    del aerialEventId[0::2] #verwijder alle even events, want per aerial event heb je per team een event
    for ID in eventId:
        if ID in aerialEventId:
            nextEventId.append(next(eventId)) #krijg de eventId van de event na het aerial event
    eventId2 = iter(eventIds)
    for ID in eventId2:
        if ID in nextEventId:
            nextnextEventId.append(next(eventId2)) #krijg de eventId van de event na het aerial event
    i = 0
    previousEventId = "0"
    previousTypeId = "0"
    for k in eventData:
        period.append(k[2])
    for event in events:
        thisEventPlayerId = event.getPlayerId()
        thisEventId = event.getId()
        thisEventTypeId = event.getTypeId()
        thisEventOutcome = event.getOutcome()
        if thisEventId in nextEventId and thisEventPlayerId != eventData[i][0]:
            if ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "0") or ((thisEventTypeId == "4" or thisEventTypeId == "44") and thisEventOutcome == "1"): 
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            elif ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "1") or ((thisEventTypeId == "4" or thisEventTypeId == "44") and thisEventOutcome == "0"): 
                minute.append(event.getMinute())            
                if event.getTeamId() == a:
                    teamEventId.append(b)
                else:
                    teamEventId.append(a)
            else:
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            previousEventId = thisEventId
            i += 1
        elif thisEventId in nextnextEventId and previousEventId not in nextEventId and previousTypeId != "5" and previousTypeId != "6" and thisEventPlayerId != eventData[i][0] and event.getTeamId == teamId[i]:
            if ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "0") or ((thisEventTypeId == "4" or thisEventTypeId == "44") and thisEventOutcome == "1"): 
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            elif ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "1") or ((thisEventTypeId == "4" or thisEventTypeId == "44") and thisEventOutcome == "0"): 
                minute.append(event.getMinute())            
                if event.getTeamId() == a:
                    teamEventId.append(b)
                else:
                    teamEventId.append(a)
            else:
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            i += 1
        elif thisEventId in nextnextEventId and previousEventId not in nextEventId and previousTypeId != "5" and previousTypeId != "6" and (thisEventPlayerId == eventData[i][0] or (thisEventPlayerId != eventData[i][0] and event.getTeamId != teamId[i])):
            if ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "1") or ((thisEventTypeId == "4" or thisEventTypeId == "44") and thisEventOutcome == "1"): 
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            elif ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "0") or ((thisEventTypeId == "4" or thisEventTypeId == "44") and thisEventOutcome == "0"): 
                minute.append(event.getMinute())            
                if event.getTeamId() == a:
                    teamEventId.append(b)
                else:
                    teamEventId.append(a)
            else:
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            i += 1
        elif thisEventId in nextnextEventId and previousEventId not in nextEventId and previousTypeId == "5" and previousTypeId == "6":
            if ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "1"): 
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            elif ((thisEventTypeId == "5" or thisEventTypeId == "6") and thisEventOutcome == "0"): 
                minute.append(event.getMinute())            
                if event.getTeamId() == a:
                    teamEventId.append(b)
                else:
                    teamEventId.append(a)
            else:
                minute.append(event.getMinute())
                teamEventId.append(event.getTeamId())
            i += 1
        else:
            previousEventId = "0"
            previousTypeId = thisEventTypeId
        
    #wonAerialDuelKeepBall = [i for i, j in zip(teamId, teamEventId) if i == j]
    compareLists = list(map(eq, teamId, teamEventId))
    array = np.column_stack((minute, teamId, teamEventId, compareLists, period, xCoordA))
    for lists in array:
        if int(lists[0]) >= timeframeEnd + timeInterval:
            time.append(timeframeStart)
            wonAerialKeepBallATotalFirst.append(wonAerialKeepBallAFirst)
            wonAerialKeepBallATotalSecond.append(wonAerialKeepBallASecond)
            wonAerialKeepBallATotalET.append(wonAerialKeepBallAET)
            wonAerialKeepBallATotal.append(wonAerialKeepBallAFirst + wonAerialKeepBallASecond + wonAerialKeepBallAET)
            wonAerialKeepBallBTotalFirst.append(wonAerialKeepBallBFirst)
            wonAerialKeepBallBTotalSecond.append(wonAerialKeepBallBSecond)
            wonAerialKeepBallBTotalET.append(wonAerialKeepBallBET)
            wonAerialKeepBallBTotal.append(wonAerialKeepBallBFirst + wonAerialKeepBallBSecond + wonAerialKeepBallBET)
            wonAerialLostBallATotalFirst.append(wonAerialLostBallAFirst)
            wonAerialLostBallATotalSecond.append(wonAerialLostBallASecond)
            wonAerialLostBallATotalET.append(wonAerialLostBallAET)
            wonAerialLostBallATotal.append(wonAerialLostBallAFirst + wonAerialLostBallASecond + wonAerialLostBallAET)
            wonAerialLostBallBTotalFirst.append(wonAerialLostBallBFirst)
            wonAerialLostBallBTotalSecond.append(wonAerialLostBallBSecond)
            wonAerialLostBallBTotalET.append(wonAerialLostBallBET)
            wonAerialLostBallBTotal.append(wonAerialLostBallBFirst + wonAerialLostBallBSecond + wonAerialLostBallBET)
            timeframeStart = timeframeStart + timeInterval
            timeframeEnd = timeframeEnd + timeInterval
            wonAerialKeepBallAFirst = 0
            wonAerialKeepBallASecond = 0
            wonAerialKeepBallAET = 0
            wonAerialKeepBallBFirst = 0
            wonAerialKeepBallBSecond = 0
            wonAerialKeepBallBET = 0
            wonAerialLostBallAFirst = 0
            wonAerialLostBallASecond = 0
            wonAerialLostBallAET = 0
            wonAerialLostBallBFirst = 0
            wonAerialLostBallBSecond = 0
            wonAerialLostBallBET = 0
        if int(lists[0]) >= timeframeEnd and int(lists[0]) > 0:
            time.append(timeframeStart)
            wonAerialKeepBallATotalFirst.append(wonAerialKeepBallAFirst)
            wonAerialKeepBallATotalSecond.append(wonAerialKeepBallASecond)
            wonAerialKeepBallATotalET.append(wonAerialKeepBallAET)
            wonAerialKeepBallATotal.append(wonAerialKeepBallAFirst + wonAerialKeepBallASecond + wonAerialKeepBallAET)
            wonAerialKeepBallBTotalFirst.append(wonAerialKeepBallBFirst)
            wonAerialKeepBallBTotalSecond.append(wonAerialKeepBallBSecond)
            wonAerialKeepBallBTotalET.append(wonAerialKeepBallBET)
            wonAerialKeepBallBTotal.append(wonAerialKeepBallBFirst + wonAerialKeepBallBSecond + wonAerialKeepBallBET)
            wonAerialLostBallATotalFirst.append(wonAerialLostBallAFirst)
            wonAerialLostBallATotalSecond.append(wonAerialLostBallASecond)
            wonAerialLostBallATotalET.append(wonAerialLostBallAET)
            wonAerialLostBallATotal.append(wonAerialLostBallAFirst + wonAerialLostBallASecond + wonAerialLostBallAET)
            wonAerialLostBallBTotalFirst.append(wonAerialLostBallBFirst)
            wonAerialLostBallBTotalSecond.append(wonAerialLostBallBSecond)
            wonAerialLostBallBTotalET.append(wonAerialLostBallBET)
            wonAerialLostBallBTotal.append(wonAerialLostBallBFirst + wonAerialLostBallBSecond + wonAerialLostBallBET)
            timeframeStart = timeframeStart + timeInterval
            timeframeEnd = timeframeEnd + timeInterval
            wonAerialKeepBallAFirst = 0
            wonAerialKeepBallASecond = 0
            wonAerialKeepBallAET = 0
            wonAerialKeepBallBFirst = 0
            wonAerialKeepBallBSecond = 0
            wonAerialKeepBallBET = 0
            wonAerialLostBallAFirst = 0
            wonAerialLostBallASecond = 0
            wonAerialLostBallAET = 0
            wonAerialLostBallBFirst = 0
            wonAerialLostBallBSecond = 0
            wonAerialLostBallBET = 0
        if lists[3] == 'True' and lists[1] == a and lists[4] == '1':
            wonAerialKeepBallAFirst += 1
        elif lists[3] == 'True' and lists[1] == a and lists[4] == '2':
            wonAerialKeepBallASecond += 1
        elif lists[3] == 'True' and lists[1] == a and (lists[4] == '3' or lists[4] == '4'):
            wonAerialKeepBallAET += 1
        elif lists[3] == 'True' and lists[1] == b and lists[4] == '1':
            wonAerialKeepBallBFirst += 1
        elif lists[3] == 'True' and lists[1] == b and lists[4] == '2':
            wonAerialKeepBallBSecond += 1
        elif lists[3] == 'True' and lists[1] == b and (lists[4] == '3' or lists[4] == '4'):
            wonAerialKeepBallBET += 1
        elif lists[3] == 'False' and lists[1] == a and lists[4] == '1':
            wonAerialLostBallAFirst += 1
        elif lists[3] == 'False' and lists[1] == a and lists[4] == '2':
            wonAerialLostBallASecond += 1
        elif lists[3] == 'False' and lists[1] == a and (lists[4] == '3' or lists[4] == '4'):
            wonAerialLostBallAET += 1
        elif lists[3] == 'False' and lists[1] == b and lists[4] == '1':
            wonAerialLostBallBFirst += 1
        elif lists[3] == 'False' and lists[1] == b and lists[4] == '2':
            wonAerialLostBallBSecond += 1
        elif lists[3] == 'False' and lists[1] == b and (lists[4] == '3' or lists[4] == '4'):
            wonAerialLostBallBET += 1
        if lists[2] == a and float(lists[5]) >= 0.0 and float(lists[5]) <= 16.0:
            zone1AWon += 1
        if lists[2] == b and float(lists[5]) >= 0.0 and float(lists[5]) <= 16.0:
            zone1BWon += 1
        if lists[2] == a and float(lists[5]) > 16.0 and float(lists[5]) <= 25.0:
            zone2AWon += 1
        if lists[2] == b and float(lists[5]) > 16.0 and float(lists[5]) <= 25.0:
            zone2BWon += 1
        if lists[2] == a and float(lists[5]) > 25.0 and float(lists[5]) <= 50.0:
            zone3AWon += 1
        if lists[2] == b and float(lists[5]) > 25.0 and float(lists[5]) <= 50.0:
            zone3BWon += 1
        if lists[2] == a and float(lists[5]) > 50.0 and float(lists[5]) <= 75.0:
            zone4AWon += 1
        if lists[2] == b and float(lists[5]) > 50.0 and float(lists[5]) <= 75.0:
            zone4BWon += 1
        if lists[2] == a and float(lists[5]) > 75.0 and float(lists[5]) <= 84.0:
            zone5AWon += 1
        if lists[2] == b and float(lists[5]) > 75.0 and float(lists[5]) <= 84.0:
            zone5BWon += 1
        if lists[2] == a and float(lists[5]) > 84.0 and float(lists[5]) <= 100.0:
            zone6AWon += 1
        if lists[2] == b and float(lists[5]) > 84.0 and float(lists[5]) <= 100.0:
            zone6BWon += 1
    time.append(timeframeStart)
    zoneAWon.extend((zone1AWon, zone2AWon, zone3AWon, zone4AWon, zone5AWon, zone6AWon))
    zoneBWon.extend((zone1BWon, zone2BWon, zone3BWon, zone4BWon, zone5BWon, zone6BWon))
    wonAerialKeepBallATotalFirst.append(wonAerialKeepBallAFirst)
    wonAerialKeepBallATotalSecond.append(wonAerialKeepBallASecond)
    wonAerialKeepBallATotalET.append(wonAerialKeepBallAET)
    wonAerialKeepBallATotal.append(wonAerialKeepBallAFirst + wonAerialKeepBallASecond + wonAerialKeepBallAET)
    wonAerialKeepBallBTotalFirst.append(wonAerialKeepBallBFirst)
    wonAerialKeepBallBTotalSecond.append(wonAerialKeepBallBSecond)
    wonAerialKeepBallBTotalET.append(wonAerialKeepBallBET)
    wonAerialKeepBallBTotal.append(wonAerialKeepBallBFirst + wonAerialKeepBallBSecond + wonAerialKeepBallBET)
    wonAerialLostBallATotalFirst.append(wonAerialLostBallAFirst)
    wonAerialLostBallATotalSecond.append(wonAerialLostBallASecond)
    wonAerialLostBallATotalET.append(wonAerialLostBallAET)
    wonAerialLostBallATotal.append(wonAerialLostBallAFirst + wonAerialLostBallASecond + wonAerialLostBallAET)
    wonAerialLostBallBTotalFirst.append(wonAerialLostBallBFirst)
    wonAerialLostBallBTotalSecond.append(wonAerialLostBallBSecond)
    wonAerialLostBallBTotalET.append(wonAerialLostBallBET)
    wonAerialLostBallBTotal.append(wonAerialLostBallBFirst + wonAerialLostBallBSecond + wonAerialLostBallBET)
    return wonAerialKeepBallATotalFirst, wonAerialKeepBallATotalSecond, wonAerialKeepBallATotalET, wonAerialKeepBallATotal, wonAerialKeepBallBTotalFirst, wonAerialKeepBallBTotalSecond, wonAerialKeepBallBTotalET, wonAerialKeepBallBTotal, wonAerialLostBallATotalFirst, wonAerialLostBallATotalSecond, wonAerialLostBallATotalET, wonAerialLostBallATotal, wonAerialLostBallBTotalFirst, wonAerialLostBallBTotalSecond, wonAerialLostBallBTotalET, wonAerialLostBallBTotal, zoneAWon, zoneBWon, time, timeInterval

def plotAerialStats(match):
    a = match.getTeams()[0].getId()
    b = match.getTeams()[1].getId()
    wonKeepAFirst, wonKeepASecond, wonKeepAET, wonKeepA, wonKeepBFirst, wonKeepBSecond, wonKeepBET, wonKeepB, wonLostAFirst, wonLostASecond, wonLostAET, wonLostA, wonLostBFirst, wonLostBSecond, wonLostBET, wonLostB, zoneAWon, zoneBWon, time, timeInterval = getAerialStats(match, a, b)
#    wonRange = range(0, ((max(wonKeepA) + max(wonKeepB)) +1), 1)
#    lostRange = range(0, ((max(wonLostA) + max(wonLostB)) +1), 1)
#    RangeMax = range(0, max(max(wonKeepA) + max(wonKeepB), max(wonLostA) + max(wonLostB)) - 1, 1)
    yticks = []
    for times in time:
        yticks.append(str(times) + ' - ' + str(times + timeInterval))
    time = np.array(time)
    width = 4

    #'Gewonnen kopduel door\n thuisploeg en bal\n behouden erna'
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    matplotlib.rcParams.update({'font.size': 18})
    ax1.barh(time, wonKeepA, width, color='#21468B')
    ax1.set_xticks(range(0,6))
    ax1.set_title('Tweede bal Nederland', y=1.03)
    ax1.set_xlabel('Aantal', ha='center', y=0.95)
    ax1.invert_xaxis()
    ax1.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax1.get_yticklabels(), visible=False)

    #'Gewonnen kopduel door\n thuisploeg, maar bal\n verloren erna'
    ax2.barh(time, wonLostA, width, color='#AE1C28')
    ax2.set_xticks(range(0,6))
    ax2.set_yticks(time)
    ax2.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax2.yaxis.set_label_coords(-0.19, 1.02)
    ax2.set_ylabel('Tijd (min)', ha='center', rotation=0, y=1.03)
    ax2.set_title('Tweede bal Denemarken', y=1.03)
    ax2.set_xlabel('Aantal', ha='center', y=0.95)
    ax2.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax2.get_yticklabels(), visible=True)
    f.subplots_adjust(wspace=0.4)
    plt.show()
    
    #'Gewonnen kopduel door\n uitploeg en bal\n behouden erna'
    g, (ax3, ax4) = plt.subplots(1, 2, sharey=True)
    ax3.barh(time, wonKeepB, width, color='#AE1C28')
    ax3.set_xticks(range(0,6))
    ax3.set_title('Tweede bal Denemarken', y=1.03)
    ax3.set_xlabel('Aantal', ha='center', y=0.95)
    ax3.invert_xaxis()
    ax3.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax3.get_yticklabels(), visible=False)

    #'Gewonnen kopduel door\n uitploeg, maar bal\n verloren erna'
    ax4.barh(time, wonLostB, width, color='#21468B')
    ax4.set_xticks(range(0,6))
    ax4.set_yticks(time)
    ax4.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax4.yaxis.set_label_coords(-0.19, 1.02)
    ax4.set_ylabel('Tijd (min)', ha='center', rotation=0, y=1.03)
    ax4.set_title('Tweede bal Nederland', y=1.03)
    ax4.set_xlabel('Aantal', ha='center', y=0.95)
    ax4.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax4.get_yticklabels(), visible=True)
    g.subplots_adjust(wspace=0.4)
    plt.show()
   
#    matplotlib.rcParams.update({'font.size': 7.5})
    sizes1 = [sum(wonKeepAFirst) + sum(wonLostBFirst), sum(wonLostAFirst) + sum(wonKeepBFirst)]
    sizes2 = [sum(wonKeepASecond) + sum(wonLostBSecond), sum(wonLostASecond) + sum(wonKeepBSecond)]
    sizes3 = [sum(wonKeepA) + sum(wonLostB), sum(wonLostA) + sum(wonKeepB)]
    sizes4 = [sum(wonKeepAET) + sum(wonLostBET), sum(wonLostAET) + sum(wonKeepBET)]
    labels = ['Nederland','Denemarken']
#    matplotlib.rcParams.update({'font.size': 10})
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
        return my_autopct
#    autotexts[0].set_fontsize(26)
#    autotexts[1].set_fontsize(26)
    patches1, texts1, autotexts1 = plt.pie(sizes1, labels=labels, colors= ['#21468B','#AE1C28'], autopct=make_autopct(sizes1),startangle=90)
    for autotext in autotexts1:
        autotext.set_color('white')
        #autotext.set_fontsize(26)
    plt.axis('equal')
    plt.show()
    patches2, texts2, autotexts2 = plt.pie(sizes2, labels=labels, colors= ['#21468B','#AE1C28'], autopct=make_autopct(sizes2),startangle=90)
    for autotext in autotexts2:
        autotext.set_color('white')
        #autotext.set_fontsize(26)
    plt.axis('equal')
    plt.show()
    patches3, texts3, autotexts3 = plt.pie(sizes3, labels=labels, colors= ['#21468B','#AE1C28'], autopct=make_autopct(sizes3),startangle=90)
    for autotext in autotexts3:
        autotext.set_color('white')
        #autotext.set_fontsize(26)
    plt.axis('equal')
    plt.show()
    if sizes4 != [0,0]:
        patches4, texts4, autotexts4 = plt.pie(sizes4, labels=labels, colors= ['#21468B','#AE1C28'], autopct=make_autopct(sizes4),startangle=90)
        for autotext in autotexts4:
            autotext.set_color('white')
            #autotext.set_fontsize(26)
        plt.axis('equal')
        plt.show()   
    
    N = 6
    M = 14 #deze kun je aanpassen
    ind = np.arange(N)
    ind2 = np.arange(M)    
    width = 0.35

    h, ax = plt.subplots()

    p1 = plt.bar(ind, zoneAWon, width, color='#21468B')
    p2 = plt.bar(ind, zoneBWon, width, color='#AE1C28', bottom=zoneAWon)
    
    xticks= ('0 - 16', '16 - 25', '25 - 50', '50 - 75', '75 - 84', '84 - 100')
    matplotlib.rcParams.update({'font.size': 22})
    ax.set_ylabel('Aantal')
    ax.set_xlabel('Hoogte op het veld t.o.v. Nederland (m)')
    ax.set_xticks(range(0,N))
    ax.set_xticklabels(xticks)
    ax.set_yticks(range(0,M,2))#en hier de 2 ook bijvoorbeeld

    plt.legend((p1[0], p2[0]), ('Nederland','Denemarken'))
    
    plt.show()