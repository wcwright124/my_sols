import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount, A):
    # TODO - you fill in here.
    def reverse(lo, hi):
        while lo < hi:
            A[lo], A[hi] = A[hi], A[lo]
            lo += 1
            hi -= 1
    rotate_amount %= len(A)
    reverse(0, len(A) - 1)
    reverse(0, rotate_amount - 1)
    reverse(rotate_amount, len(A) - 1)
    return 


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rotate_array.py", 'rotate_array.tsv',
                                       rotate_array_wrapper))
