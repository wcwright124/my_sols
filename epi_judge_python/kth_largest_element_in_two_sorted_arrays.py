from test_framework import generic_test


def find_kth_in_two_sorted_arrays(A, B, k):
    # TODO - you fill in here.
    if len(B) < len(A):
        A, B = B, A
    lo = max(0, k - len(B))
    hi = min(k, len(A))
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        leftA = A[mid - 1] if mid > 0 else float('-inf')
        rightA = A[mid] if mid < len(A) else float('inf')
        idx = k - mid
        leftB = B[idx - 1] if idx > 0 else float('-inf')
        rightB = B[idx] if idx < len(B) else float('inf')
        if rightA < leftB:
            lo = mid + 1
        elif leftA > rightB:
            hi = mid - 1
        else:
            return max(leftA, leftB)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "kth_largest_element_in_two_sorted_arrays.py",
            'kth_largest_element_in_two_sorted_arrays.tsv',
            find_kth_in_two_sorted_arrays))
