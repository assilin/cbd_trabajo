#!/usr/bin/python

import sys

current_player = None
total_made = 0
total_missed = 0
average_free_throw = 0
limit_value = 0.9

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    player, state = data_mapped

    if current_player == player:
        if state == "make":
            total_made += 1
        else:
            total_missed += 1
    else:
        if current_player:
            average_free_throw = total_made / (total_made + total_missed)
            if average_free_throw >= limit_value:
                print(f'{current_player}\t{average_free_throw}')

        current_player = player
        total_made = 1 if state == "make" else 0
        total_missed = 0 if state == "make" else 1

if current_player:
    average_free_throw = total_made / (total_made + total_missed)
    if average_free_throw > limit_value:
        print(f'{current_player}\t{average_free_throw}')
