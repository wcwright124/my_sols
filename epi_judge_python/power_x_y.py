from test_framework import generic_test


def power(x: float, y: int) -> float:
    # TODO - you fill in here.
    if y < 0:
        return power(1.0 / x, -y)
    res = 1.0
    while y:
        if y & 1:
            res *= x
        x *= x
        y >>= 1
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
