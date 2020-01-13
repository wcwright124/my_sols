import math
from test_framework import generic_test


def square_root(x):
    # TODO - you fill in here.
    if x < 1.0:
        lo, hi = 0, 1.0
    else:
        lo, hi = 1.0, x
    
    while not math.isclose(lo, hi):
        y = 0.5 * (lo + hi)
        if y ** 2 > x:
            hi = y
        else:
            lo = y
    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
