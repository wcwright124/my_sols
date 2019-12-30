from test_framework import generic_test

# let n = # of bits 
def add(x, y): # O(n) time | O(1) space
    if x < y:
        x, y = y, x
    while y:
        x, y = (x^y), (x&y) << 1
    return x

def multiply(x, y): # O(n ** 2) time | O(1) space
    # TODO - you fill in here.
    if x < y:
        x, y = y, x
    res = 0
    while y:
        if y & 1:
            res = add(res, x)
        x <<= 1
        y  >>= 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
                                       
