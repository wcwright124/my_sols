import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream):
    # TODO - you fill in here.
    num_bucket = 1 << 16
    counter = [0] * num_bucket
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part = x >> 16
        counter[upper_part] += 1

    bucket_capacity = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < bucket_capacity)
    candidates = [0] * bucket_capacity

    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1
        
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i
    return 0


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
