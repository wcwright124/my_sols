from test_framework import generic_test


def matrix_search(A, x): # O(n + m) time | O (1) space
    # TODO - you fill in here.
    n, m = len(A), len(A[0])
    i, j = 0, m - 1
    while 0 <= i < n and 0 <= j < m:
        if A[i][j] == x:
            return True
        elif A[i][j] < x:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
