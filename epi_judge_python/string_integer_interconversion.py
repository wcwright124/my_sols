from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return '0'
    elif x < 0:
        return '-' + int_to_string(-x)
    digitStrings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = []
    while x:
        res.append(digitStrings[x % 10])
        x //= 10
    res.reverse()
    return ''.join(res)


def string_to_int(s):
    # TODO - you fill in here.
    if not s:
        return 0
    start_idx = 0
    isNegative = (s[0] == '-')
    if s[0] in ('+', '-'):
        start_idx += 1
    res = 0
    for i in range(start_idx, len(s)):
        c = s[i]
        res = 10 * res + ord(c) - ord('0')
    if isNegative:
        res = -res
    return res


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
