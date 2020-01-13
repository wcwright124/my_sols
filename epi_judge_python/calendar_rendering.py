import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    start_times = [a.start for a in A]
    start_times.sort()
    end_times = [a.finish for a in A]
    end_times.sort()
    start_idx, end_idx = 0, 0
    max_sim = 0
    curr_sim = 0
    while start_idx < len(A):
        if start_times[start_idx] <= end_times[end_idx]:
            curr_sim += 1
            start_idx += 1
        else:
            curr_sim -= 1
            end_idx += 1
        max_sim = max(max_sim, curr_sim)
    return max(max_sim, curr_sim)


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
