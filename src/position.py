from src.exception_position import PositionInvalidException
from src.position_interface import PositionInterface

cardinal_set = {'N': 'North', 'S': 'South', 'W': 'West', 'E': 'East'}


class Position(PositionInterface):
    """
    Position of a Rover (x, y, cardinal). 
    """

    def __init__(self, x, y, cardinal):
        """
        Constructor of a Position
        :param x: Position x Axis
        :param y: Position y Axis
        :param cardinal: Cardinal compass point
        """
        self.x = int(x)
        self.y = int(y)
        if (self.x >= 0 and self.y >= 0) and (cardinal in cardinal_set.keys()):
            self.cardinal = cardinal
        else:
            raise PositionInvalidException(x, y, cardinal)

    def __str__(self):
        """
        String to print
        """
        return str(self.x)+' ' + str(self.y)+' '+str(self.cardinal)

    def __eq__(self, position):
        return (self.x == position.x and self.y == position.y)
