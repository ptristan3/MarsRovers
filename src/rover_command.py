import logging
from abc import abstractmethod
from src.exception_command import CommandInvalidException


command_set = ['M', 'L', 'R']


class RoverCommand(object):
    """
    Command accepted by Rovers
    """

    def __init___(self, command):
        if command in command_set:
            self.RoverCommand = command
        else:
            raise CommandInvalidException(command)

    def __str__(self):
        """
        String to print
        """
        return str(self.RoverCommand)

    @abstractmethod
    def execute(self, position):
        pass
