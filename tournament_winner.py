def tournamentWinner(competitions, results):
    # Write your code here.
    teams = {x : 0 for x in {x for l in competitions for x in l}}
    for i in range(0,len(results)):
        if results[i] == 0:
            teams[competitions[i][1]] = teams[competitions[i][1]] + 3
        else:
            teams[competitions[i][0]] = teams[competitions[i][0]] + 3
    #for i in competitions
    return max(teams, key=teams.get)

  
competition = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results = [0,0,1]
tournamentWinner(competition,results)
