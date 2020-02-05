import collections

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray1(A): # O(n) time | O(1) space
    # TODO - you fill in here.
    max_lis_len = prev_lis_len = curr_lis_len = 1
    start = end = 0
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            curr_lis_len = 1 + prev_lis_len
            if curr_lis_len > max_lis_len:
                start, end = i - curr_lis_len + 1, i
                max_lis_len = curr_lis_len
            prev_lis_len = curr_lis_len
        else:
            prev_lis_len = 1
    return Subarray(start, end)

# Official Solution uses skipping to improve best-case performance
def find_longest_increasing_subarray(A):
    res = Subarray(0, 0)
    i, max_length = 0, 1
    while i < len(A) - max_length:
        for j in range(i + max_length, i, -1):
            if A[j - 1] >= A[j]:
                i = j
                break
        else:
            i += max_length
            while i < len(A) and A[i - 1] < A[i]:
                i, max_length = i + 1, max_length + 1
            res = Subarray(i - max_length, i - 1)
    return res


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_increasing_subarray.py",
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
