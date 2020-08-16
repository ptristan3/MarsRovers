import logging
import builtins
from src.command_factory import produce
from src.exception_position import *
from src.exception_plateau import PlateauInvalidDimmensionException
from src.exception_command import CommandInvalidException
from src.plateau import Plateau
from src.position import Position
from src.rover import Rover


def parse_input_model_file(input_model_file):
    """
    From the input file, build a Plateau and put on
    the rovers.
    :param inputModelFile: FileName 
    """
    logging.info("Building ...")
    model_file = builtins.open(input_model_file)
    plateau_size = model_file.readline()
    id_rover = 1
    rovers_data = model_file.readlines()
    rovers_data.reverse()
    rovers = list()
    logging.info("The size of Plateau: %s x %s",
                 plateau_size.split()[0], plateau_size.split()[1])
    try:
        plateau = Plateau(plateau_size.split()[0], plateau_size.split()[1])
        while (len(rovers_data) > 0):
            rover_position_line = rovers_data.pop()
            (x, y, c) = rover_position_line.split()
            rover_commands_line = rovers_data.pop().replace('\n', '')
            try:
                rover_mission = produce(rover_commands_line)
                new_rover = Rover(id_rover, Position(x, y, c), rover_mission)
                logging.info("Rover %s", str(new_rover))
                if not plateau.is_busy_position(new_rover.position):
                    plateau.add_rover(new_rover)
                else:
                    logging.info("Initial Position ( %s ) of Rover %d is busy. Rover not added",
                                 new_rover.position, new_rover.id_number)

                id_rover += 1
            except (PositionInvalidException, CommandInvalidException) as e:
                logging.info(
                    "Into parser of input. Exception: %s", str(e.message))
        return plateau
    except PlateauInvalidDimmensionException as e:
        logging.info("Into parser of input. Exception: %s", str(e.message))
