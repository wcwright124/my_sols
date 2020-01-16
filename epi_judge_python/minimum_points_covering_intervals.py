import collections
import functools
import typing

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    # TODO - you fill in here.
    intervals.sort(key=lambda x: x.right)
    visit_time = typing.cast(int, float('-inf'))
    num_visits = 0
    for interval in intervals:
        if interval.left > visit_time:
            visit_time = interval.right
            num_visits += 1
    return num_visits


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
