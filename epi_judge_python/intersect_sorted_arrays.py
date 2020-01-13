from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    if len(B) < len(A):
        A, B = B, A
    res = []
    iA, iB = 0, 0
    while iA < len(A) and iB < len(B):
        if A[iA] == B[iB]:
            if not res:
                res.append(A[iA])
            elif res[-1] != A[iA]:
                res.append(A[iA])
            iA += 1
            iB += 1
        elif A[iA] < B[iB]:
            iA += 1
        else:
            iB += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
