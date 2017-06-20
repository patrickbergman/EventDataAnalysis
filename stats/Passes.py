from helpers.colors import Colors

def printTotalTeamPasses(match):
    for team in match.getTeams():
        successFullPasses = 0
        passes = team.getEventsByEventId(1)
        offsidePasses = team.getEventsByEventId(2)
        totalPasses = passes + offsidePasses
        for playerPass in totalPasses:
            if playerPass.getOutcome() == 1:
                successFullPasses = successFullPasses + 1
        passesPercentage = (successFullPasses / totalPasses) * 100
        print(Colors.YELLOW, end='')
        print(team.getName(), end='')
        print(Colors.WHITE, end='')
        print(": " + len(totalPasses) + " passes", end='')
        print("(" + passesPercentage + "% successfull)")