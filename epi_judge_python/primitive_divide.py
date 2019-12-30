from test_framework import generic_test


def divide(x, y):
    # TODO - you fill in here.
    res, pow = 0, 32
    y_pow = y << pow
    while x >= y:
        while y_pow > x:
            y_pow >>= 1
            pow -= 1
        res += 1 << pow
        x -= y_pow
    return res
    #return 0 if x < y else 1 + divide(x-y, y)


if __name__ == '__main__':
    print(divide(4, 2))
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
