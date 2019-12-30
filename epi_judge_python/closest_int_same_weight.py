from test_framework import generic_test

def lowest_set_bit(x):
    return x & ~(x-1)

def lowest_unset_bit(x):
    return ~x & (x + 1)

def closest_int_same_bit_count(x):
    # TODO - you fill in here.
    s = lowest_set_bit(x)
    ns = lowest_unset_bit(x)
    if ns > s:
        x |= ns
        x ^= ns >> 1
    else:
        x ^= s
        x |= s >> 1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
