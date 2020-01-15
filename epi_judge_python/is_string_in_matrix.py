import functools

from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def is_valid(i, j, k):
        if k == len(S):
            return True
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])) or grid[i][j] != S[k]:
            return False
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        return any([is_valid(x,y,k+1) for x,y in neighbors])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_valid(i, j, 0):
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
