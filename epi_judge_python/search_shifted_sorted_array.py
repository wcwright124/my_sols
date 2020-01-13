from test_framework import generic_test


def search_smallest(A):
    # TODO - you fill in here.
    if not A:
        return None
    if len(A) == 1 or A[0] < A[-1]:
        return 0
    
    lo, hi = 1, len(A) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if A[mid] > A[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
