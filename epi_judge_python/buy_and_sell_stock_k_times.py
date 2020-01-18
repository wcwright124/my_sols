from test_framework import generic_test


def buy_and_sell_stock_k_times(prices, k):
    # TODO - you fill in here.
    dp = [[-1 for _ in prices] for _ in range(k+1)]
    dp[0] = [0 for _ in prices]
    min_so_far = prices[0]
    dp[1][0] = 0
    for i in range(1, len(prices)):
        dp[1][i] = max(prices[i] - min_so_far, dp[1][i-1])
        min_so_far = min(min_so_far, prices[i])
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_k_times.py",
                                       'buy_and_sell_stock_k_times.tsv',
                                       buy_and_sell_stock_k_times))
