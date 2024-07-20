import matplotlib.pyplot as plt
import requests


def getwinloss(season=0, includePost=False, team='all'):
	teamstemp = ['Portland Sunsets', 'Baltimore Mob', 'New York Rats', 'Pacific Ocean Prawns', 'Dublin Seasons',
	             'Transports', 'Kansas City Mints', 'Fresno Femboys', 'Seattle Seals', 'Boston Bee Boys',
	             'Denver Killers',
	             'Sox Puppets']

	if season == 0:
		url = 'https://daseballapi.adaptable.app/games'
	else:
		url = 'https://daseballapi.adaptable.app/games/' + str(season)
	response = requests.get(url)
	data = response.json()
	teams = []
	number = -5
	for team in teamstemp:
		teams.append([team, '', [number/20]])
		number += 1
		for game in data:
			if game['homeTeam']['teamName'] == team:
				teams[-1][1] = game['homeTeam']['teamColor']
			elif game['awayTeam']['teamName'] == team:
				teams[-1][1] = game['awayTeam']['teamColor']
	for n, team in enumerate(teams):
		for game in data:
			if game['homeTeam']['gamesPlayed'] <= 20 or (includePost and season == 0):
				if game['homeTeam']['teamName'] == team[0]:
					if game['homeScore'] > game['awayScore']:
						teams[n][2].append(1)
					else:
						teams[n][2].append(-1)
				elif game['awayTeam']['teamName'] == team[0]:
					if game['awayScore'] > game['homeScore']:
						teams[n][2].append(1)
					else:
						teams[n][2].append(-1)
	for n, team in enumerate(teams):
		sumation = 0
		for x in range(len(team[2])):
			sumation += team[2][x]
			teams[n][2][x] = sumation

	for team in teams:
		plt.plot(team[2], label=team[0], color='#' + team[1])
	plt.legend()
	plt.xlabel('Game Number')
	plt.ylabel('Win/Loss')
	plt.locator_params(axis='both', integer=True)
	plt.title('Win/Loss record for all teams')
	plt.show()
