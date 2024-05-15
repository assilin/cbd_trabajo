#!/usr/bin/python

# Format of each line is:
# URL,GameType,Location,Date,Time,WinningTeam,Quarter,SecLeft,AwayTeam,AwayPlay,AwayScore,HomeTeam,HomePlay,HomeScore,Shooter,ShotType,ShotOutcome,ShotDist,Assister,Blocker,FoulType,Fouler,Fouled,Rebounder,ReboundType,ViolationPlayer,ViolationType,TimeoutTeam,FreeThrowShooter,FreeThrowOutcome,FreeThrowNum,EnterGame,LeaveGame,TurnoverPlayer,TurnoverType,TurnoverCause,TurnoverCauser,JumpballAwayPlayer,JumpballHomePlayer,JumpballPoss


import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if data:
        shooter = data[14]
        type_shot = data[15]
        result_shot = data[16]
        free_throw_shooter = data[28]
        result_free_throw = data[29]

        output_shooter = None
        output_score = 0

        if shooter and result_shot == "make":
            output_shooter = shooter
            if "2-pt" in type_shot:
                output_score = 2
            elif "3-pt" in type_shot:
                output_score = 3
        elif free_throw_shooter and result_free_throw == "make":
            output_shooter = free_throw_shooter
            output_score = 1

        if output_score and output_shooter:
            print(f"{output_shooter}\t{output_score}")
