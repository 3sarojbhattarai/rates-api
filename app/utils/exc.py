

class RegionDoesNotError(Exception):
    """ Exception if the given region does not have port """

    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return self.msg
