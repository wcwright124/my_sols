import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # TODO - you fill in here.
    # remove all b's
    a_count, b_count = 0, 0
    write_idx = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'b':
            b_count += 1
        if s[i] == 'a':
            a_count += 1
    # replace a's with 'dd'
    left, right = write_idx - 1, size + a_count - b_count - 1
    while left >= 0:
        if s[left] == 'a':
            s[right] = 'd'
            right -= 1
            s[right] = 'd'
        else:
            s[right] = s[left]
        left -= 1
        right -= 1
    return size + a_count - b_count


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
