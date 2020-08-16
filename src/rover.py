from src.position import Position
from src.exception_position import *
from src.rover_interface import RoverInterface
import logging


class Rover(RoverInterface):
    """ 
    The Rover as the vehicle that move into Plateau
    """

    def __init__(self, number, position, mission):
        """
        Constructor of a Rover
        :param number: Identifier of a rover
        :param position: Initial position
        :param mission: Set of rover's command
        """
        self.id_number = number
        self.position = position
        self.mission = mission

    def __str__(self):
        """
        String to print
        """
        return 'Rover: '+str(self.id_number)+' => Position: ('+str(self.position) + ') Mission: '+self.print_mission()

    def __eq__(self, rover):
        return self.id_number == rover.id_number

    def __ne__(self, rover):
        return not(self.id_number == rover.id_number)

    def execute_one_command(self, command, plateau):
        """
        Execute only a command into the plateau.
        :param command: The instruction to be excecuted
        :param plateau: Plateau where the rove's command is excecuted
        """
        new_position = command.execute(self.position)
        if plateau.is_valid_move(self.id_number, new_position):
            self.position = new_position
        else:
            raise PositionNotFoundException(new_position)

    def print_mission(self):
        """
        Print the sequence of command.
        """
        command_list = ''
        for command in self.mission:
            command_list = command_list + str(command)
        return command_list

    def process_mission(self, plateau):
        """ 
        Rover mission execution into the plateau.
        A mission is a string of commands.
        :param plateau: Plateau where the mission is excecuted
        """
        logging.info("Rover Number %d", self.id_number)

        for command in self.mission:
            new_position = command.execute(self.position)

            logging.info("Inicial Position %d %d %s, Command %s , Final Position %d %d %s", self.position.x, self.position.y,
                         self.position.cardinal, str(command), new_position.x, new_position.y, new_position.cardinal)

            if plateau.is_valid_position(self.id_number, new_position):
                self.position = new_position
            else:
                raise PositionNotFoundException(new_position)

                logging.info(
                    "Mission of Rover Number %d has finished", self.id_number)
