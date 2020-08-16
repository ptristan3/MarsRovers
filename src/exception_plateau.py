class PlateauInvalidDimmensionException(Exception):
    """
    Thrown when dimmension of Plateau are not valid.
    """

    def __init__(self, w, h):
        self.message = "Position {} is not valid".format(w).format(h)
        super(PlateauInvalidDimmensionException, self).__init__()
