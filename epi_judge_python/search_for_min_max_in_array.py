import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

def find_min_max_bf(A):
    return MinMax(min(A), max(A))

def find_min_max(A):
    # TODO - you fill in here.
    def get_min_max_pair(x, y):
        if x <= y:
            return x, y
        else:
            return y, x
    if not A:
        return None
    if len(A) == 1:
        return MinMax(A[0], A[0])

    _min, _max = get_min_max_pair(A[0], A[1])
    
    for i in range(2, len(A) - 1, 2):
        a, b = get_min_max_pair(A[i], A[i + 1])
        _min = min(_min, a)
        _max = max(_max, b)

    if len(A) % 2 == 1:
        if A[-1] < _min:
            _min = A[-1]
        elif A[-1] > _max:
            _max = A[-1]

    return MinMax(_min, _max)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
