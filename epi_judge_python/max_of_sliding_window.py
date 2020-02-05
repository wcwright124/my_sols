import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume


def calculate_traffic_volumes(A, w):
    # TODO - you fill in here.
    A.sort(key = lambda x: x.time)
    res = []
    queue = collections.deque()
    for a in A:
        t, vol = a.time, a.volume
        while queue and t - queue[0].time > w:
            queue.popleft()
        while queue and vol >= queue[-1].volume:
            queue.pop()
        queue.append(a)
        res.append(TrafficElement(t, queue[0].volume))
    return res


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_of_sliding_window.py",
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
