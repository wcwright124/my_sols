import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    def reverse(left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    s.reverse()
    i = 0
    for j, c in enumerate(s):
        if c == ord(' '):
            reverse(i, j-1)
            i = j + 1
        elif j == len(s) - 1:
            reverse(i, j)
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
