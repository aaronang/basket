from itertools import tee


def pairs(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)