import copy

from test_framework import generic_test


def rook_attack(A):
    # TODO - you fill in here.
    n, m = len(A), len(A[0])
    rook_in_first_row = (0 in A[0])
    rook_in_first_col = any(A[i][0] == 0 for i in range(n))
    for i in range(1, n):
        for j in range(1, m):
            if A[i][j] == 0:
                A[0][j] = 0
                A[i][0] = 0
    # zero rows
    for i in range(1, n):
        if A[i][0] == 0:
            for j in range(1, m):
                A[i][j] = 0
    # zero cols
    for j in range(1, m):
        if A[0][j] == 0:
            for i in range(1, n):
                A[i][j] = 0
    
    if rook_in_first_row:
        for j in range(m):
            A[0][j] = 0
    if rook_in_first_col:
        for i in range(n):
            A[i][0] = 0
    return


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rook_attack.py", 'rook_attack.tsv',
                                       rook_attack_wrapper))
