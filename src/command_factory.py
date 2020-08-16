from src.rover_command import RoverCommand, command_set
from src.turn_left_command import TurnLeft
from src.turn_right_command import TurnRight
from src.move_forward_command import MoveForward
from src.exception_command import CommandInvalidException


def produce(commands):
    mission = list()
    for command in commands:
        if command in command_set:
            if command is 'M':
                mission.append(MoveForward())
            elif command is 'R':
                mission.append(TurnRight())
            elif command is 'L':
                mission.append(TurnLeft())
        else:
            raise CommandInvalidException(command)
    return mission
