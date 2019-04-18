import sys

def print_error(*args, **kwargs):
    """ Prints into standrad error """
    print(*args, file=sys.stderr, **kwargs)