import heapq

from test_framework import generic_test

# heap solution from epi
# less efficient thatn solution below
# O(n log n) time | O(n) space
def calculate_bonus_heap(productivity): # O (n log n) time | O(n) space
    min_heap = [(p, i) for i, p in enumerate(productivity)]
    heapq.heapify(min_heap)
    ticks = [1] * len(productivity)
    while min_heap:
        curr_dev = heapq.heappop(min_heap)[1]
        if curr_dev > 0 and productivity[curr_dev] > productivity[curr_dev - 1]:
            ticks[curr_dev] = ticks[curr_dev - 1] + 1
        if curr_dev + 1 < len(ticks) and productivity[curr_dev] > productivity[curr_dev + 1]:
            ticks[curr_dev] = max(ticks[curr_dev], 1 + ticks[curr_dev + 1])
    return sum(ticks)


def calculate_bonus(productivity): # O(n) time | O(n) space
    # TODO - you fill in here.
    ticks = [1 for _ in productivity]
    for i in range(1, len(productivity)):
        if productivity[i] > productivity[i - 1]:
            ticks[i] = 1 + ticks[i - 1]
    for i in range(len(productivity) - 2, -1, -1):
        if productivity[i] > productivity[i + 1]:
            ticks[i] = max(ticks[i], 1 + ticks[i + 1])
    return sum(ticks)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bonus.py", 'bonus.tsv',
                                       calculate_bonus))
