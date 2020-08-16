from src.rover_command import RoverCommand
from src.position import Position

#from RoverCommand import RoverCommand
#from position import Position


to_right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}

class TurnRight(RoverCommand):
  """
  Turn Right 90Grad command
  """

  def __init__(self):
    """
    Constructor Turn Right Command
    """
    self.RoverCommand = 'R'

  def __str__(self):
    """
    String to print
    """
    return str(self.RoverCommand)

  def execute(self, position):
    """
    Implement execute function to TurnRight
    The rotation function is defined by toRight map
    """
    return Position(position.x, position.y,to_right[position.cardinal])