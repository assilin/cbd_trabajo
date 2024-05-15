#!/usr/bin/python

import sys

total_score = 0
current_player = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    player, points = data_mapped

    if current_player and current_player != player:
        print(f"{current_player}\t{total_score}")
        total_score = 0

    current_player = player
    total_score += int(points)

if current_player is not None:
    print(f"{current_player}\t{total_score}")
