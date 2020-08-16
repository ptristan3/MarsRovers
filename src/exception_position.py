class PositionInvalidException(Exception):
    """
    Thrown when position x or y are not valid.
    """

    def __init__(self, x, y, cardinal):
        self.message = "Position {} {} {} is not valid".format(x, y, cardinal)
        super(PositionInvalidException, self).__init__()


class PositionNotFoundException(Exception):
    """
    Thrown when a Position on the Plateau is not valid.
    """

    def __init__(self, position):
        self.message = "Postion {} is not valid for the Plateau".format(
            position)
        super(PositionNotFoundException, self).__init__()


class PositionBusyException(Exception):
    """
    Thrown when a Position into Plateau is busy by another rover.
    """

    def __init__(self, position):
        self.message = "Postion {} is busy by another rover".format(position)
        super(PositionNotFoundException, self).__init__()
