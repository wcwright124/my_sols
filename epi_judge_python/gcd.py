from test_framework import generic_test

def gcd(x, y): # cleaner form of 24.1
    num_shifts = 0
    while x != 0:
        if x > y:
            x, y = y, x
        elif not x&1 and not y&1:
            num_shifts += 1
            x >>= 1
            y >>= 1
        elif not x&1 and y&1:
            x >>= 1
        elif x&1 and not y&1:
            y >>= 1
        else:
            y -= x
    return y << num_shifts


def gcd2(x, y): # 24.1 no mult, div, or mod
    assert (x >= 0) and (y >= 0)
    if x == y:
        return x
    if x == 0:
        return y
    if y == 0:
        return x
    
    num_shifts = 0
    while (x&1 == 0) and (y&1 == 0):
        num_shifts += 1
        x >>= 1
        y >>= 1
    while x&1 == 0:
        x >>= 1
    while y&1 == 0:
        y >>= 1
    
    while x != y:
        if y > x:
            temp = x
            while y > temp:
                temp <<= 1
            temp >>= 1
            y -= temp
        else: # y < x
            temp = y
            while x > temp:
                temp <<= 1
            temp >>= 1
            x -= temp
    return x << num_shifts

def gcd1(x, y):
    # TODO - you fill in here.
    if y > x:
        x, y = y, x
    return x if y == 0 else gcd(y, x % y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
