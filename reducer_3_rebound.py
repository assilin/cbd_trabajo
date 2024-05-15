#!/usr/bin/python

import sys

current_rebounder = None
total_rebounds = 0
games = set()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    rebounder, game_id = data_mapped

    if current_rebounder == rebounder:
        total_rebounds += 1
        games.add(game_id)
    else:
        if current_rebounder:
            average_rebounds = round(total_rebounds / len(games), 2)
            print(f'{current_rebounder}\t{average_rebounds}')

        current_rebounder = rebounder
        total_rebounds = 1
        games = {game_id}

if current_rebounder is not None:
    average_rebounds = total_rebounds / len(games)
    print(f'{current_rebounder}\t{average_rebounds}')
