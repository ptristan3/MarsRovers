from src.rover_command import RoverCommand
from src.position import Position

#from RoverCommand import RoverCommand
#from position import Position

to_left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}

class TurnLeft(RoverCommand):
  """ 
  Turn Left 90Grad command 
  """

  def __init__(self):
    """
    Constructor Turn Left Command
    """
    self.RoverCommand = 'L'

  def __str__(self):
    """
    String to print
    """
    return str(self.RoverCommand)

  def execute(self, position):
    """
    Implement execute function to TurnLeft
    The rotation function is defined by toLeft map
    """
    return Position(position.x,  position.y, to_left[position.cardinal])