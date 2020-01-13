from test_framework import generic_test


def longest_contained_range(A):
    # TODO - you fill in here.
    A_set = set(A)
    res = 0
    while A_set:
        x = A_set.pop()
        curr_len = 1
        temp = x + 1
        while temp in A_set:
            curr_len += 1
            A_set.remove(temp)
            temp += 1
        temp = x - 1
        while temp in A_set:
            curr_len += 1
            A_set.remove(temp)
            temp -= 1
        res = max(res, curr_len)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
