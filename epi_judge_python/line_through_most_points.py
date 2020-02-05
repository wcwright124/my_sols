import collections
import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Point = collections.namedtuple("Point", ("x", "y"))


def find_line_with_most_points(points):
    # TODO - you fill in here.
    res = 0
    for i, p1 in enumerate(points):
        counts = collections.Counter()
        same_count = 1
        for j in range(i + 1, len(points)):
            p2 = points[j]
            if p1 == p2:
                same_count += 1
            elif p1.x == p2.x:
                counts[(1, 0)] += 1
            else:
                dy, dx = p2.y - p1.y, p2.x - p1.x
                gcf = math.gcd(dy, dx)
                dy /= gcf
                dx /= gcf
                if dx < 0:
                    dx, dy = -dx, -dy
                counts[(dy, dx)] += 1
        res = max(res, same_count + max(counts.values(), default = 0))
    return res


@enable_executor_hook
def find_line_with_most_points_wrapper(executor, points):
    points = [Point(*x) for x in points]
    return executor.run(functools.partial(find_line_with_most_points, points))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("line_through_most_points.py",
                                       'line_through_most_points.tsv',
                                       find_line_with_most_points_wrapper))
