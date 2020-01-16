import collections
import functools

from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step): # O(nk) time | O(k) space
    ans = collections.deque()
    for _ in range(min(top, maximum_step)):
        ans.append(1 + sum(ans))
    for _ in range(top - maximum_step):
        ans.append(sum(ans))
        ans.popleft()
    return ans.pop()


def number_of_ways_to_top2(top, maximum_step): # O(nk) time | O(n) space
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def helper(n, k):
        if n < 0:
            return 0
        if n == 0:
            return 1
        res = 0
        for i in range(1, k + 1):
            res += helper(n-i, k)
        return res
    return helper(top, maximum_step)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
