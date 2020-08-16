class CommandInvalidException(Exception):
    """
    Thrown when the command is not valid for the rover.
    """

    def __init__(self, command):
        self.message = "Command {} is not valid".format(command)
        super(CommandInvalidException, self).__init__()
