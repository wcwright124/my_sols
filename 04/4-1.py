""" Write expressions that use bitwise operators, equality checks, 
and Boolean operators to do the following in O(1) time.
- right propagate the rightmost set bit in x, e.g. turns
    (01010000) into (01011111)
- compute x mod a power of two, e.g. returns 13 for 77 mod 64.
- tests if x is a power of 2, i.e, evaluates to true for x = 1, 2, 4, 8, ...
    false for all other values.
"""

def right_prop(x):
    return x | (x - 1)

def mod(x, p):
    if p == 1:
        return x
    return x & (p - 1)

def isPowerOf2(x):
    return x & (x-1) == 0


if __name__ == '__main__':
    print(isPowerOf2(16)) # True
    print(isPowerOf2(64)) # True
    print(isPowerOf2(831)) # False
    print(mod(77, 64)) # 13
    print(right_prop(80))