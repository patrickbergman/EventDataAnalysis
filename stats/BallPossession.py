from core.colorama import init, Fore
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

init()


def __createDataFrame(match):
    timeline = pd.DataFrame(columns=['id', 'teamId', 'minutes', 'seconds', 'totalSeconds', 'timestamp'])
    for event in match.getEvents():
        if (event.getTypeId() != '30' or event.getTypeId() != '32'):  # Do not include events with start or end game as eventId
            timeline = timeline.append({
                "id": event.getId(),
                "teamId": event.getTeamId(),
                "minutes": int(event.getMinute()),
                "seconds": int(event.getSecond()),
                "totalSeconds": int(event.getMinute()) * 60 + int(event.getSecond()),
                "timestamp": event.getTimestamp()
            }, ignore_index=True)

    timeline['ballPossession'] = (timeline.totalSeconds - timeline.totalSeconds.shift(1)).shift(-1)

    # TODO per zone?
    # print (__teamComposition(timeline))
    return timeline


def __teamComposition(match, dataFrame):
    teamComposition = dataFrame.teamId.unique()
    return teamComposition


def createTimeLine(dataFrame):
    fig, ax = plt.subplots()
    ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='blue')
    ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                   facecolors=('red', 'yellow', 'green'))
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('seconds since start')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Bill', 'Jim'])
    ax.grid(True)
    ax.annotate('race interrupted', (61, 25),
                xytext=(0.8, 0.9), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=16,
                horizontalalignment='right', verticalalignment='top')

    plt.show()


def percentagePossession(match):
    df = __createDataFrame(match)
    teamComposition = __teamComposition(match, df)

    totalBallPossession = sum(df['ballPossession'].loc[df['ballPossession'] > 0])
    ballPosessionA = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[0]) & (df['ballPossession'] > 0)])
    ballPosessionB = sum(df['ballPossession'].loc[(df['teamId'] == teamComposition[1]) & (df['ballPossession'] > 0)])

    print(Fore.BLUE + 'Total ball possession in seconds', totalBallPossession)
    print(Fore.YELLOW + 'Ball possession in percentage')
    print('Team', match.findTeamById(teamComposition[0]).getName(), ': ', ballPosessionA / totalBallPossession * 100, '%', ' and in seconds: ',
          ballPosessionA)
    print('Team', match.findTeamById(teamComposition[1]).getName(), ': ', ballPosessionB / totalBallPossession * 100, '%', ' and in seconds: ',
          ballPosessionB)


def intervalPossession(match):
    df = __createDataFrame(match)
    teamComposition = __teamComposition(match, df)

    # TEAM A DETAILS
    total0_5secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 0) & (df['ballPossession'] <= 5)]
    total5_10secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 6) & (df['ballPossession'] <= 10)]
    total10_15secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 11) & (df['ballPossession'] <= 15)]
    total15_20secondsA = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 16) & (df['ballPossession'] <= 20)]
    total20secondsA = df['ballPossession'].loc[(df['teamId'] == teamComposition[0]) & (df['ballPossession'] >= 21)]

    firstIntervalA = sum(total0_5secondsA) / len(total0_5secondsA)
    secondIntervalA = sum(total5_10secondsA) / len(total5_10secondsA)
    thirdIntervalA = sum(total10_15secondsA) / len(total10_15secondsA)
    fourthIntervalA = sum(total15_20secondsA) / len(total15_20secondsA)
    fifthIntervalA = sum(total20secondsA) / len(total20secondsA)

    # TEAM B DETAILS
    total0_5secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 0) & (df['ballPossession'] <= 5)]
    total5_10secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 6) & (df['ballPossession'] <= 10)]
    total10_15secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 11) & (df['ballPossession'] <= 15)]
    total15_20secondsB = df['ballPossession'].loc[
        (df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 16) & (df['ballPossession'] <= 20)]
    total20secondsB = df['ballPossession'].loc[(df['teamId'] == teamComposition[1]) & (df['ballPossession'] >= 21)]

    firstIntervalB = sum(total0_5secondsB) / len(total0_5secondsB)
    secondIntervalB = sum(total5_10secondsB) / len(total5_10secondsB)
    thirdIntervalB = sum(total10_15secondsB) / len(total10_15secondsB)
    fourthIntervalB = sum(total15_20secondsB) / len(total15_20secondsB)
    fifthIntervalB = sum(total20secondsB) / len(total20secondsB)

    print(Fore.BLUE + 'Average ball possession per interval in seconds')
    print(Fore.YELLOW + 'Team ', teamComposition[0], 'and ', Fore.GREEN + 'Team ', teamComposition[1] + ': ')
    print(Fore.RED + '0 - 5 seconds: ', Fore.YELLOW + str(firstIntervalA), Fore.GREEN + str(firstIntervalB))
    print(Fore.RED + '5 - 10 seconds: ', Fore.YELLOW + str(secondIntervalA), Fore.GREEN + str(secondIntervalB))
    print(Fore.RED + '10 - 15 seconds: ', Fore.YELLOW + str(thirdIntervalA), Fore.GREEN + str(thirdIntervalB))
    print(Fore.RED + '15 - 20 seconds: ', Fore.YELLOW + str(fourthIntervalA), Fore.GREEN + str(fourthIntervalB))
    print(Fore.RED + '20+ seconds: ', Fore.YELLOW + str(fifthIntervalA), Fore.GREEN + str(fifthIntervalB))


def zonePossession(match):
    dataFrame = __createDataFrame(match)