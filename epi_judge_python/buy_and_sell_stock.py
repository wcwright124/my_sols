from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    max_profit = 0.0
    min_so_far = prices[0]
    for i in range(1, len(prices)):
        current_profit = prices[i] - min_so_far
        max_profit = max(current_profit, max_profit)
        min_so_far = min(min_so_far, prices[i])
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
