from src.rover_command import RoverCommand
from src.position import Position


class MoveForward(RoverCommand):
    """
    Move forward into Plateau according Cardinal Point
    """

    def __init__(self):
        """
        Constructor MoveForwardCommand
        """
        self.command_rover = 'M'

    def __str__(self):
        """
        String to print
        """
        return str(self.command_rover)

    def execute(self, position):
        """
        Implement execute function to MoveForward
        The move forward +1 depend of de Cardinal Point
        """
        if (position.cardinal == 'N'):
            return Position(position.x, position.y+1, position.cardinal)
        elif (position.cardinal == 'W'):
            return Position(position.x-1, position.y, position.cardinal)
        elif (position.cardinal == 'E'):
            return Position(position.x+1, position.y, position.cardinal)
        elif (position.cardinal == 'S'):
            return Position(position.x, position.y-1, position.cardinal)