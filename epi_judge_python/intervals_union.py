import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

class Solution:
    def __overlaps(self, i1, i2):
        left_val = max(i1.left.val, i2.left.val)
        right_val = min(i1.right.val, i2.right.val)

        if left_val < right_val:
            return True
        elif left_val == right_val:
            if i1.right.val == i2.left.val:
                return (i1.right.is_closed or i2.left.is_closed)
            elif i1.left.val == i2.right.val:
                return (i1.left.is_closed or i2.right.is_closed)
            else:
                return False
        else:
            return False

    def __union(self, i1, i2):
        left_val = min(i1.left.val, i2.left.val)
        right_val = max(i1.right.val, i2.right.val)
        
        if i1.left.val == i2.left.val:
            left_is_closed = i1.left.is_closed or i2.left.is_closed
        elif i1.left.val < i2.left.val:
            left_is_closed = i1.left.is_closed
        else:
            left_is_closed = i2.left.is_closed
        
        if i1.right.val == i2.right.val:
            right_is_closed = i1.right.is_closed or i2.right.is_closed
        elif i1.right.val < i2.right.val:
            right_is_closed = i2.right.is_closed
        else:
            right_is_closed = i1.right.is_closed

        left_endpoint = Endpoint(left_is_closed, left_val)
        right_endpoint = Endpoint(right_is_closed, right_val)

        return Interval(left_endpoint, right_endpoint)
    
    def union_of_intervals(self, intervals):
        intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if self.__overlaps(interval, res[-1]):
                res[-1] = self.__union(interval, res[-1])
            else:
                res.append(interval)
        return res

    def test(self):
        left1 = Endpoint(False, 176)
        right1 = Endpoint(False, 183)
        left2 = Endpoint(True, 183)
        right2 = Endpoint(True, 192)
        interval1 = Interval(left1, right1)
        interval2 = Interval(left2, right2)
        print(self.__overlaps(interval1, interval2))
        union = self.__union(interval1, interval2)
        print(union)

def union_of_intervals(intervals):
    sol = Solution()
    res = sol.union_of_intervals(intervals)
    # TODO - you fill in here.
    return res


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
