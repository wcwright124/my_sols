import bisect

from test_framework import generic_test


def search_first_of_k_bisect(A, k):
    # TODO - you fill in here.
    idx = bisect.bisect_left(A, k)
    if 0 <= idx < len(A) and A[idx] == k:
        return idx
    return -1

def search_first_of_k(A, k):
    res = -1
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] < k:
            lo = mid + 1
        elif A[mid] > k:
            hi = mid - 1
        else:
            res = mid
            hi = mid - 1
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
