def tournamentWinner(competitions, results):
    currWinner = ""
    dict = {currWinner:0}
    for i, team in enumerate(competitions):
        if results[i] == 0:
            if team[1] not in dict:
                dict[team[1]] = 1
            else:
                dict[team[1]] += 1
            if dict[team[1]] > dict[currWinner]:
                currWinner = team[1]
        if results[i] == 1:
            if team[0] not in dict:
                dict[team[0]] = 1
            else:
                dict[team[0]] += 1
            if dict[team[0]] > dict[currWinner]:
                currWinner = team[0]
    return currWinner
