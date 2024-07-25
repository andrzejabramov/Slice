from math import inf


def divide(first, second):
    try:
        res = first / second
        return res
    except ZeroDivisionError:
        return inf

