#!/usr/bin/python

# Format of each line is:
# URL,GameType,Location,Date,Time,WinningTeam,Quarter,SecLeft,AwayTeam,AwayPlay,AwayScore,HomeTeam,HomePlay,HomeScore,Shooter,ShotType,ShotOutcome,ShotDist,Assister,Blocker,FoulType,Fouler,Fouled,Rebounder,ReboundType,ViolationPlayer,ViolationType,TimeoutTeam,FreeThrowShooter,FreeThrowOutcome,FreeThrowNum,EnterGame,LeaveGame,TurnoverPlayer,TurnoverType,TurnoverCause,TurnoverCauser,JumpballAwayPlayer,JumpballHomePlayer,JumpballPoss


import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if data:
        rebounder = data[23]
        type_rebound = data[24]
        # game_id = date + home_team + away_team
        game_id = (data[3] + data[8] + data[11]).replace(" ", "")

        if rebounder and rebounder != "Team" and type_rebound == "defensive":
            print(f"{rebounder}\t{game_id}")
