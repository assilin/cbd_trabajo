#!/usr/bin/python

# Format of each line is:
# URL,GameType,Location,Date,Time,WinningTeam,Quarter,SecLeft,AwayTeam,AwayPlay,AwayScore,HomeTeam,HomePlay,HomeScore,Shooter,ShotType,ShotOutcome,ShotDist,Assister,Blocker,FoulType,Fouler,Fouled,Rebounder,ReboundType,ViolationPlayer,ViolationType,TimeoutTeam,FreeThrowShooter,FreeThrowOutcome,FreeThrowNum,EnterGame,LeaveGame,TurnoverPlayer,TurnoverType,TurnoverCause,TurnoverCauser,JumpballAwayPlayer,JumpballHomePlayer,JumpballPoss


import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if data:
        free_throw_shooter = data[28]
        result_free_throw = data[29]

    if free_throw_shooter is not None:
        print(f'{free_throw_shooter}\t{result_free_throw}')
