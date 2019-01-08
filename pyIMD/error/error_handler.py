__author__ = 'Andreas P. Cuny'


class ArgumentError(Exception):
    """
    Argument Error class prints error to console.

    Args:
        msg ('str')         Error message
    """
    def __init__(self, msg):
        print(msg)

