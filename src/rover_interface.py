from src.position import Position
from src.exception_position import *
from abc import abstractmethod
import logging


class RoverInterface():
    """ 
    The Rover Interfaces Class
    """
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, rover):
        pass

    @abstractmethod
    def __ne__(self, rover):
        pass

    @abstractmethod
    def process_mission(self, plateau):
        """ 
        Rover mission execution into the plateau.
        A mission is a string of commands.
        :param plateau: Plateau where the mission is excecuted
        """
        pass
