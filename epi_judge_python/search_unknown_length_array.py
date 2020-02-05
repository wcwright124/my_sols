from test_framework import generic_test


def binary_search_unknown_length(A, k):
    # TODO - you fill in here.
    p = 0
    while True:
        try:
            idx = (1 << p) - 1
            if A[idx] == k:
                return idx
            elif A[idx] > k:
                break
        except IndexError:
            break
        p += 1
    lo, hi = 1 << max(p - 1, 0), (1 << p) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        try:
            if A[mid] == k:
                return mid
            elif A[mid] < k:
                lo = mid + 1
            else:
                hi = mid - 1
        except IndexError:
            hi = mid - 1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_unknown_length_array.py",
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
