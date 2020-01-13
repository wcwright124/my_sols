import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    def union(i1, i2):
        return Interval(min(i1.left, i2.left), max(i1.right, i2.right))
    
    def less_than(i1, i2):
        return i1.right < i2.left
    
    def overlaps(i1, i2):
        return max(i1.left, i2.left) <= min(i1.right, i2.right)
    
    # TODO - you fill in here.
    res = []
    idx = 0
    merged = new_interval
    
    while idx < len(disjoint_intervals):
        if less_than(disjoint_intervals[idx], new_interval):
            res.append(disjoint_intervals[idx])
            idx += 1
        else:
            break
    
    while idx < len(disjoint_intervals) and overlaps(disjoint_intervals[idx], new_interval):
        merged = union(disjoint_intervals[idx], merged)
        idx += 1
    res.append(merged)
    
    while idx < len(disjoint_intervals):
        res.append(disjoint_intervals[idx])
        idx += 1
    
    return res


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
