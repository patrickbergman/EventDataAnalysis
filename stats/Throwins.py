import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def isForward(event):
    angle = float(event.findQualifierByQualifierId(213).getValue())

    if angle > 1.57 and angle < 4.17:
        return False
    else:
        return True

def getLocation(event):
    # returns 0 for 0-24.99, 1 for 25-49.99, 2 for 50-74.99, 3 for 75-100
    x = float(event.getXCoordinate())
    if x < 25:
        return 0
    elif x < 50:
        return 1
    elif x < 75:
        return 2
    else:
        return 3

def getStats(throwins):

    forwardWin = [0,0,0,0]
    forwardLose = [0,0,0,0]
    backwardWin = [0,0,0,0]
    backwardLose = [0,0,0,0]

    for event in throwins:
        if isForward(event):
            if event.getOutcome() == "1":
                forwardWin[getLocation(event)] += 1
            else:
                forwardLose[getLocation(event)] += 1
        else:
            if event.getOutcome() == "1":
                backwardWin[getLocation(event)] += 1
            else:
                backwardLose[getLocation(event)] += 1

    return forwardWin, forwardLose, backwardWin, backwardLose

def printThrowins(match):
    a = match.getTeams()[0]
    b = match.getTeams()[1]
    print(match.getTeams()[0].getName() + ":" + "blue")
    print(match.getTeams()[1].getName() + ":" + "red")
    throwinsA = a.findEventsByQualifierId(107)
    throwinsB = b.findEventsByQualifierId(107)

    # 0 = 0-25, 1 = 25-50, 2 = 50-75, 3 = 75-100
    forwardWinA, forwardLoseA, backwardWinA, backwardLoseA = getStats(throwinsA)
    forwardWinB, forwardLoseB, backwardWinB, backwardLoseB = getStats(throwinsB)

    backwardRange = max(backwardWinA) + max(backwardLoseA)
    forwardRange = max(forwardWinA) + max(forwardLoseA)
    xRange = range(0, max([backwardRange,forwardRange]) + 1, 2)

    yticks = ['0 - 25', '25 - 50', '50 - 75', '75 - 100']
    metres = [0,20,40,60]
    metres = np.array(metres)
    width = 5

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    matplotlib.rcParams.update({'font.size': 26})
    ax1.barh(metres, backwardWinA, width, label='Behouden', color='#21468B')
    ax1.barh(metres, backwardLoseA, width, left=backwardWinA, label='Afgestaan', color='#21468B', alpha=0.5)
    ax1.set_xticks(xRange)
    ax1.set_title('Achteruit', y=1.03)
    ax1.set_xlabel('Aantal inworpen', ha='center', y=0.95)
    ax1.legend()
    ax1.invert_xaxis()
    ax1.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax1.get_yticklabels(), visible=False)

    ax2.barh(metres, forwardWinA, width, label='Behouden', color='#21468B')
    ax2.barh(metres, forwardLoseA, width, left=forwardWinA, label='Afgestaan', color='#21468B', alpha=0.5)
    ax2.set_xticks(xRange)
    ax2.set_yticks(metres)
    ax2.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax2.yaxis.set_label_coords(-0.19, 1.02)
    ax2.set_ylabel('Locatie (m)', ha='center', rotation=0, y=1.03)
    ax2.set_title('Vooruit', y=1.03)
    ax2.set_xlabel('Aantal inworpen', ha='center', y=0.95)
    ax2.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax2.get_yticklabels(), visible=True)
    f.subplots_adjust(wspace=0.4)
    plt.show()

    backwardRange = max(backwardWinB) + max(backwardLoseB)
    forwardRange = max(forwardWinB) + max(forwardLoseB)
    xRange = range(0, max([backwardRange,forwardRange]) + 1, 2)

    g, (ax3, ax4) = plt.subplots(1, 2, sharey=True)
    ax3.barh(metres, backwardWinB, width, label='Behouden', color='#AE1C28')
    ax3.barh(metres, backwardLoseB, width, left=backwardWinB, label='Afgestaan', color='#AE1C28', alpha=0.5)
    ax3.set_xticks(xRange)
    ax3.set_title('Achteruit', y=1.03)
    ax3.set_xlabel('Aantal inworpen', ha='center', y=0.95)
    ax3.legend()
    ax3.invert_xaxis()
    ax3.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax3.get_yticklabels(), visible=False)

    ax4.barh(metres, forwardWinB, width, label='Behouden', color='#AE1C28')
    ax4.barh(metres, forwardLoseB, width, left=forwardWinB, label='Afgestaan', color='#AE1C28', alpha=0.5)
    ax4.set_xticks(xRange)
    ax4.set_yticks(metres)
    ax4.set_yticklabels(yticks, ha='center', position=(-0.19, 0))
    ax4.yaxis.set_label_coords(-0.19, 1.02)
    ax4.set_ylabel('Locatie (m)', ha='center', rotation=0, y=1.03)
    ax4.set_title('Vooruit', y=1.03)
    ax4.set_xlabel('Aantal inworpen', ha='center', y=0.95)
    ax4.tick_params(axis=u'y', which=u'both', length=0)
    plt.setp(ax4.get_yticklabels(), visible=True)
    g.subplots_adjust(wspace=0.4)
    plt.show()