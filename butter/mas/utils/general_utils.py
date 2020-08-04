import sys


def print_error(*args, **kwargs):
    """ Prints into standard error """
    print(*args, file=sys.stderr, **kwargs)
