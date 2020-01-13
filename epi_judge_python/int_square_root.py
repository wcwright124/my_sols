from test_framework import generic_test


def square_root(k):
    # TODO - you fill in here.
    res = 0
    lo, hi = 0, k
    while lo <= hi:
        x = lo + (hi - lo) // 2
        if x ** 2 == k:
            return x
        elif x ** 2 < k:
            res = max(res, x)
            lo = x + 1
        else:
            hi = x - 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
