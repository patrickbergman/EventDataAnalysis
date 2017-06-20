from helpers.colors import Colors

def printTotalTeamPasses(match):
    for team in match.getTeams():
        successFullPasses = 0
        passes = team.getEventsByTypeId(1)
        offsidePasses = team.getEventsByTypeId(2)
        if passes is None and offsidePasses is None:
            totalPasses = 0
        elif passes is None and offsidePasses is not None:
            totalPasses = offsidePasses
        elif passes is not None and offsidePasses is None:
            totalPasses = passes
        else:
            totalPasses = passes + offsidePasses

        for playerPassEvent in totalPasses:
            if playerPassEvent.getOutcome() == '1':
                successFullPasses = successFullPasses + 1
        passesPercentage = (successFullPasses / len(totalPasses)) * 100
        print(Colors.YELLOW, end='')
        print(team.getName(), end='')
        print(Colors.WHITE, end='')
        print(": " + str(len(totalPasses)) + " passes (", end='')
        print("%.2f" % round(passesPercentage, 2), end='')
        print("% successfull)")