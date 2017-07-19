from core.colorama import init, Fore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

init()


# Calls the initialized functions, to create dataframe and make array team composition
def createDataframe(match):
    df = __createDataFrame(match)
    teamComposition = __teamComposition(match, df)
    print(Fore.RED + 'Dataframe is created.')
    return df, teamComposition


# Initialize and create dataframe
def __createDataFrame(match):
    timeline = pd.DataFrame(columns=['id', 'teamId', 'minutes', 'seconds', 'totalSeconds', 'timestamp'])
    for event in match.getEvents():
        # if event.findQualifierByQualifierId('56') != None:
        # print(event.findQualifierByQualifierId('56').getValue())

        # if event.hasPlayer():
        #    print(event.getPlayer().getFullName())
        if (event.getTypeId() != 30 or event.getTypeId() != 32) and (
            event.findQualifierByQualifierId(56) != None) and (
        event.hasPlayer()):  # Do not include events with start or end game as eventId
            timeline = timeline.append({
                "id": event.getId(),
                "teamId": event.getTeamId(),
                "minutes": int(event.getMinute()),
                "seconds": int(event.getSecond()),
                "totalSeconds": int(event.getMinute()) * 60 + int(event.getSecond()),
                "zone": event.findQualifierByQualifierId(56).getValue(),
                "timestamp": event.getTimestamp(),
                "player": event.getPlayer().getFullName()
            }, ignore_index=True)

    timeline['ballPossession'] = (timeline.totalSeconds - timeline.totalSeconds.shift(1)).shift(-1)
    return timeline


# Determine the teams and put in an array
def __teamComposition(match, dataFrame):
    teamComposition = dataFrame.teamId.unique()
    return teamComposition


# Percentage of ball posession per team, during a complete match
def percentagePossession(match, df, teamComposition):
    # df = __createDataFrame(match)
    # teamComposition = __teamComposition(match, df)

    totalBallPossession = sum(df['ballPossession'].loc[df['ballPossession'] > 0])
    ballPossessionA = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[0]) & (df['ballPossession'] > 0)])
    ballPossessionB = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[1]) & (df['ballPossession'] > 0)])

    print(Fore.BLUE + 'Total ball possession in seconds', totalBallPossession)
    print(Fore.YELLOW + 'Ball possession in percentage')
    print('Team', match.findTeamById(teamComposition[0]).getName(), ': ',
          round(ballPossessionA / totalBallPossession * 100, 2), '%', ' and in seconds: ', ballPossessionA)
    print('Team', match.findTeamById(teamComposition[1]).getName(), ': ',
          round(ballPossessionB / totalBallPossession * 100, 2), '%', ' and in seconds: ', ballPossessionB)


# Ball possession per team in %, per interval
def intervalPossession(match, df, teamComposition):
    # df = __createDataFrame(match)
    # teamComposition = __teamComposition(match, df)

    totalPossessionA = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[0]) & (df['ballPossession'] > 0)])
    totalPossessionB = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[1]) & (df['ballPossession'] > 0)])

    # TEAM A DETAILS
    total0_5secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 0) & (df['ballPossession'] < 5)]
    total5_10secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 5) & (df['ballPossession'] < 10)]
    total10_15secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 10) & (df['ballPossession'] < 15)]
    total15_20secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 15) & (df['ballPossession'] < 20)]
    total20secondsA = df['ballPossession'].loc[(df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 20)]

    firstIntervalA = round(sum(total0_5secondsA) / totalPossessionA * 100, 2)
    secondIntervalA = round(sum(total5_10secondsA) / totalPossessionA * 100, 2)
    thirdIntervalA = round(sum(total10_15secondsA) / totalPossessionA * 100, 2)
    fourthIntervalA = round(sum(total15_20secondsA) / totalPossessionA * 100, 2)
    fifthIntervalA = round(sum(total20secondsA) / totalPossessionA * 100, 2)

    # TEAM B DETAILS
    total0_5secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 0) & (df['ballPossession'] < 5)]
    total5_10secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 5) & (df['ballPossession'] < 10)]
    total10_15secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 10) & (df['ballPossession'] < 15)]
    total15_20secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 15) & (df['ballPossession'] < 20)]
    total20secondsB = df['ballPossession'].loc[(df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 20)]

    firstIntervalB = round(sum(total0_5secondsB) / totalPossessionB * 100, 2)
    secondIntervalB = round(sum(total5_10secondsB) / totalPossessionB * 100, 2)
    thirdIntervalB = round(sum(total10_15secondsB) / totalPossessionB * 100, 2)
    fourthIntervalB = round(sum(total15_20secondsB) / totalPossessionB * 100, 2)
    fifthIntervalB = round(sum(total20secondsB) / totalPossessionB * 100, 2)

    print(Fore.BLUE + 'Ball possession per interval in percentage')
    print(Fore.YELLOW + 'Team ', match.findTeamById(teamComposition[0]).getName(), 'and ', Fore.GREEN + 'Team ',
          match.findTeamById(teamComposition[1]).getName() + ': ')
    print(Fore.RED + '0 - 5 seconds: ', Fore.YELLOW + str(firstIntervalA) + '%', Fore.GREEN + str(firstIntervalB) + '%')
    print(Fore.RED + '5 - 10 seconds: ', Fore.YELLOW + str(secondIntervalA) + '%',
          Fore.GREEN + str(secondIntervalB) + '%')
    print(Fore.RED + '10 - 15 seconds: ', Fore.YELLOW + str(thirdIntervalA) + '%',
          Fore.GREEN + str(thirdIntervalB) + '%')
    print(Fore.RED + '15 - 20 seconds: ', Fore.YELLOW + str(fourthIntervalA) + '%',
          Fore.GREEN + str(fourthIntervalB) + '%')
    print(Fore.RED + '20+ seconds: ', Fore.YELLOW + str(fifthIntervalA) + '%', Fore.GREEN + str(fifthIntervalB) + '%')

    teamA = [firstIntervalA, secondIntervalA, thirdIntervalA, fourthIntervalA, fifthIntervalA]
    teamB = [firstIntervalB, secondIntervalB, thirdIntervalB, fourthIntervalB, fifthIntervalB]
    return teamA, teamB


# Decide player with longest ball possession per team
def bestPlayerPossession(match, df, teamComposition):
    # df = __createDataFrame(match)
    # teamComposition = __teamComposition(match, df)
    bestPlayer = pd.DataFrame()

    players = df.player.unique()
    bestPlayer['player'] = players
    bestPlayer = bestPlayer.set_index('player')
    bestPlayer['player'] = players

    for i in players:
        bestPlayer.set_value(i, 'possession',
                             sum(df['ballPossession'].loc[(df['player'] == i) & (df['ballPossession'] > 0)]))
        bestPlayer.set_value(i, 'teamId', df['teamId'].loc[(df['player'] == i)].unique()[0])
    print(bestPlayer)
    bestPlayerA = max(bestPlayer['possession'].loc[bestPlayer['teamId'] == teamComposition[0]])
    bestPlayerB = max(bestPlayer['possession'].loc[bestPlayer['teamId'] == teamComposition[1]])

    print(Fore.GREEN + 'Player with most ball possession per team')
    print(Fore.BLUE + 'Team: ', match.findTeamById(teamComposition[0]).getName(), Fore.BLUE,
          bestPlayer['player'].loc[bestPlayer['possession'] == bestPlayerA])
    print(Fore.GREEN + 'With ball possession of: ', bestPlayerA, 'seconds')
    print(Fore.BLUE + 'Team: ', match.findTeamById(teamComposition[1]).getName(), Fore.BLUE,
          bestPlayer['player'].loc[bestPlayer['possession'] == bestPlayerB])
    print(Fore.GREEN + 'With ball possession of: ', bestPlayerB, 'seconds')


# Determines ball possession per team, per zone in %
def zonePossession(match, df, teamComposition):
    # df = __createDataFrame(match)
    # teamComposition = __teamComposition(match, df)

    totalPossessionA = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[0]) & (df['ballPossession'] > 0)])
    totalPossessionB = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[1]) & (df['ballPossession'] > 0)])

    # TEAM A DETAILS
    totalRightA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['zone'] == 'Right') & (df['ballPossession'] > 0)]
    totalLeftA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['zone'] == 'Left') & (df['ballPossession'] > 0)]
    totalCenterA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['zone'] == 'Center') & (df['ballPossession'] > 0)]
    totalBackA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['zone'] == 'Back') & (df['ballPossession'] > 0)]

    rightA = round(sum(totalRightA) / totalPossessionA * 100, 2)
    leftA = round(sum(totalLeftA) / totalPossessionA * 100, 2)
    centerA = round(sum(totalCenterA) / totalPossessionA * 100, 2)
    backA = round(sum(totalBackA) / totalPossessionA * 100, 2)

    # TEAM B DETAILS
    totalRightB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['zone'] == 'Right') & (df['ballPossession'] > 0)]
    totalLeftB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['zone'] == 'Left') & (df['ballPossession'] > 0)]
    totalCenterB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['zone'] == 'Center') & (df['ballPossession'] > 0)]
    totalBackB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['zone'] == 'Back') & (df['ballPossession'] > 0)]

    rightB = round(sum(totalRightB) / totalPossessionB * 100, 2)
    leftB = round(sum(totalLeftB) / totalPossessionB * 100, 2)
    centerB = round(sum(totalCenterB) / totalPossessionB * 100, 2)
    backB = round(sum(totalBackB) / totalPossessionB * 100, 2)

    print(Fore.BLUE + 'Ball possession per zone in percentage')
    print(Fore.YELLOW + 'Team ', match.findTeamById(teamComposition[0]).getName(), 'and ', Fore.GREEN + 'Team ',
          match.findTeamById(teamComposition[1]).getName() + ': ')
    print(Fore.RED + 'Right zone: ', Fore.YELLOW + str(rightA) + '%', Fore.GREEN + str(rightB) + '%')
    print(Fore.RED + 'Left zone: ', Fore.YELLOW + str(leftA) + '%', Fore.GREEN + str(leftB) + '%')
    print(Fore.RED + 'Center zone: ', Fore.YELLOW + str(centerA) + '%', Fore.GREEN + str(centerB) + '%')
    print(Fore.RED + 'Back zone: ', Fore.YELLOW + str(backA) + '%', Fore.GREEN + str(backB) + '%')


# Makes histogram of ball possession per interval in %
def histogramPossession(match, dataFrame, teamComposition):
    teamA, teamB = intervalPossession(match, dataFrame, teamComposition)
    N = 5

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars
    ax = plt.gca()
    # 21468B
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, teamA, width, color='#21468B')

    #    rects2 = ax.bar(ind, teamB, width, color='#AE1C28')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Frequentie (%)')
    ax.set_xticks(ind)
    plt.ylim(0, 50)
    ax.set_xlabel('Tijd (secondes)')
    ax.set_xticklabels(('0-5', '5-10', '10-15', '15-20', '20+'))

    # ax.legend((rects1[0], rects2[0]), (match.findTeamById(teamComposition[0]).getName(), match.findTeamById(teamComposition[1]).getName()))

    autolabel(rects1)
    #    autolabel(rects2)

    plt.show()


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    ax = plt.gca()

    for rect in rects:
        height = rect.get_height()

        ax.text(rect.get_x() + rect.get_width() / 2., 1 * height,
                '%1.1f' % round(height, 2),
                ha='center', va='bottom')


