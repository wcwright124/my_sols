import functools

from test_framework import generic_test


def maximum_revenue(coins):
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def solve(i, j):
        if i > j:
            return 0
        choose_left = coins[i] + min(solve(i + 2, j), solve(i + 1, j - 1)) 
        choose_right = coins[j] + min(solve(i, j - 2), solve(i + 1, j - 1))
        return max(choose_left, choose_right)
    return solve(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
