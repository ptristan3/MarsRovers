import logging
from src.exception_position import PositionNotFoundException
from src.exception_plateau import PlateauInvalidDimmensionException


class Plateau:
    """
    Grid of Mars Plateau
    """

    def __init__(self, widht, height):
        """
        Constructor of a Plateau
        :param widht: Number of columns of Grid
        :param height: Number of rows of Grid
        """
        self.width = int(widht)
        self.height = int(height)
        self.rovers = list()
        if (self.width < 0 or self.height < 0):
            raise PlateauInvalidDimmensionException(self.width, self.height)

    def __str__(self):
        """
        String to print
        """
        return 'Plateau Dimmension: (' + str(self.width) + ', ' + str(self.height) + ')'

    def is_in_range(self, position):
        """
        Return if a position is valid into the PLateau
        :param postion: position to compare
        """
        return (position.x >= 0 and position.y >= 0 and
                position.x <= self.width and position.y <= self.height)

    def is_busy_position(self, position):
        """
        Return if a position is actually busy for another rover
        :param postion: position to check x and y axis
        """
        ret = False
        for rover in self.rovers:
            if rover.position == position:
                ret = True
        return ret

    def is_valid_position(self, current_rover_id, position):
        """
        Return if a new position of currentRover is valid.
        If the new position of the current rover is in a valid
        range of the plateau and is not busy by another rover.
        :param current_rover_id: rover id to check position
        :param postion: position to check
        """
        if self.is_in_range(position):
            for rover in self.rovers:
                if current_rover_id != rover.id_number:
                    if rover.position == position:
                        return False
            return True
        else:
            return False

    def add_rover(self, rover):
        """
        Add a new rover at the set of rovers
        :param rover: A new rover to add
        """
        if not self.is_busy_position(rover.position):
            self.rovers.append(rover)

    def print_position_rover(self, rover):
        """
        Print the position of a rover
        :param rover: Rover to print
        """
        print(rover.id_number + rover.position)

    def print_position_rovers(self):
        """
        Print the position of all rovers into the plateau
        """
        for rover in self.rovers:
            print("Rover:" + str(rover.id_number) +
                  " Position:" + str(rover.position))

    def run(self):
        """
        Excecute all missions of all rovers into plateau.
        Each mission of each rover is excecuted according to the plateau state 
        """
        logging.info("The Plateau start to run...")
        for rover in self.rovers:
            try:
                rover.process_mission(self)
            except PositionNotFoundException as exception:
                print(str(exception.message))
                logging.info("Into plateu.run(). Exception: %s",
                             str(exception.message))
        logging.info("The Plateau has finished to run all missions...")
