import functools

from test_framework import generic_test

def number_of_ways_bottom_up(n, m):
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

def number_of_ways(n, m): # O(nm) time | O(nm) space
    @functools.lru_cache(None)
    def num_ways_helper(x, y):
        if x == 1 or y == 1:
            return 1
        return num_ways_helper(x - 1, y) + num_ways_helper(x, y - 1)
    # TODO - you fill in here.
    return num_ways_helper(n, m)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways_bottom_up))
