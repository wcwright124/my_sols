from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    if x < 0:
        return -reverse(-x)
    res = 0
    while x:
        res = 10 * res + (x % 10)
        x //= 10
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
