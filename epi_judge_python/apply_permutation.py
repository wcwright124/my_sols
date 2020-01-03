from test_framework import generic_test


def apply_permutation2(perm, A): # O(n) time | O(n) space
    # TODO - you fill in here.
    A_copy = A[:]
    for i in range(len(perm)):
        j = perm[i]
        A[j] = A_copy[i]
    return A

def apply_permutation3(perm, A): # O(n) time | O(1) space
    for i in range(len(perm)):
        while perm[i] != i:
            j = perm[i]
            A[i], A[j] = A[j], A[i]
            perm[i], perm[j] = perm[j], perm[i]
    return A

def apply_permutation(perm, A): # O(n) time | O(1) space
    temp = perm[:]
    for i in range(len(perm)):
        if perm[i] >= 0:
            v, j = A[i], perm[i]
            while j != i:
                A[j], v = v, A[j]
                perm[j], j = ~perm[j], perm[j]
            A[i] = v
        else:
            perm[i] = ~perm[i]
    assert perm == temp
    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
