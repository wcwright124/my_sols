from test_framework import generic_test

def buy_and_sell_stock_once(prices, start_idx = 0, end_idx = None):
    if end_idx is None:
        end_idx = len(prices) - 1
    max_profit = 0.0
    min_so_far = prices[start_idx]
    for i in range(start_idx+1, end_idx + 1):
        current_profit = prices[i] - min_so_far
        max_profit = max(current_profit, max_profit)
        min_so_far = min(min_so_far, prices[i])
    return max_profit

def buy_and_sell_stock_twice(prices): # O(n) time | O(n) space
    # TODO - you fill in here.
    p1 = [0.0] * len(prices) # contains best buy and sell at or before day i
    min1 = prices[0]
    for i in range(1, len(prices)):
        p1[i] = max(p1[i-1], prices[i] - min1)
        min1 = min(min1, prices[i])

    p2 = [0.0] * len(prices) # max profit buying on or after day i
    max2 = prices[-1]
    for i in range(len(prices)-2, -1, -1):
        p2[i] = max(p2[i+1], max2 - prices[i])
        max2 = max(max2, prices[i])
    
    ans = 0.0
    for i in range(len(prices)):
        ans = max(ans, p1[i] + p2[i])
    return ans

def buy_and_sell_stock_twice2(prices): # O(n) time | O(1) space, incorrect
    best = [(0.0, 0), (0.0, 0)]
    min_so_far = prices[0]
    buy_idx = 0
    for i in range(1, len(prices)):
        current_profit = prices[i] - min_so_far
        if current_profit > best[1][0]:
            if buy_idx == best[1][1]:
                best[1] = (current_profit, buy_idx)
            else:
                best[0] = best[1]
                best[1] = (current_profit, buy_idx)
        elif current_profit > best[0][0]:
            best[0] = (current_profit, buy_idx)
        if prices[i] <= min_so_far:
            buy_idx = i
            min_so_far = prices[i]
    return best[0][0] + best[1][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
