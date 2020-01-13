from test_framework import generic_test


def smallest_nonconstructible_value(A):
    # TODO - you fill in here.
    if not A:
        return 1
    A.sort()
    cum_sum = 0
    for a in A:
        if a > cum_sum + 1:
            return cum_sum + 1
        cum_sum += a
    return cum_sum + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
