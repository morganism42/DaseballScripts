import requests
import json
import matplotlib.pyplot as plt


def GetERA(data: list[dict], player):
	playerData = [[0, 0, 0]]
	for game in data:
		if game['homePitcher']['name'] == player:
			score = game['awayScore']
			innings = game['inningNumber']
			playerData.append([score + playerData[-1][0], innings + playerData[-1][1], game['gameDay']])
		elif game['awayPitcher']['name'] == player:
			score = game['homeScore']
			innings = game['inningNumber']
			playerData.append([score + playerData[-1][0], innings + playerData[-1][1], game['gameDay']])
	ERA = [0]
	gameday = [0]
	for game in playerData[1:]:
		ERA.append((9 * game[0]) / game[1])
		gameday.append(game[2])
	return [ERA, gameday]


def get_stat(stat='ERA', player='Berry Sting', season=3):
	url = 'https://daseballapi.adaptable.app/games/' + str(season)
	response = requests.get(url)
	data = response.json()
	# print(data)
	if stat == 'ERA':
		value = GetERA(data, player)
		label = player + "'s ERA over season " + str(season)
		plt.plot(value[1], value[0])
		plt.title(label)
		plt.show()
