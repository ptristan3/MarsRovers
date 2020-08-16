from abc import abstractmethod

class PositionInterface():
  """
  Position interface of a Rover. 
  """
  @abstractmethod
  def __str__(self):
    pass

  @abstractmethod
  def __eq__(self, position):
    pass