from test_framework import generic_test


def rotate_matrix(square_matrix):
    # TODO - you fill in here.
    n = len(square_matrix)
    # transpose
    for i in range(n):
        for j in range(i+1, n):
            square_matrix[i][j], square_matrix[j][i] = square_matrix[j][i], square_matrix[i][j]
    # reverse rows
    for i in range(n):
        square_matrix[i].reverse()
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
