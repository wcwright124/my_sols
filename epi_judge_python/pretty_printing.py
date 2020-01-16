import functools
import typing

from test_framework import generic_test


def minimum_messiness(words, line_length):
    @functools.lru_cache(None)
    def min_messiness_helper(end_idx):
        if end_idx < 0:
            return 0
        remaining_space = line_length - len(words[end_idx])
        ans = remaining_space ** 2 + min_messiness_helper(end_idx - 1)
        for j in range(end_idx - 1, -1, -1):
            remaining_space -= len(words[j]) + 1
            if remaining_space < 0:
                break
            ans = min(ans, remaining_space ** 2 + min_messiness_helper(j - 1))
        return ans
    # TODO - you fill in here.
    return min_messiness_helper(len(words) - 1)


if __name__ == '__main__':
    """
    tests = [
        [["aaa", "bbb", "c", "d", "ee"], 11]
    ]
    for t in tests:
        words, line_length = t
        print(minimum_messiness(words, line_length))
    """
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))#"""
