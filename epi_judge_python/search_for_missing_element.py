import functools
import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    # TODO - you fill in here.
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)
    lsb, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    for i, a in enumerate(A):
        if i & lsb:
            miss_or_dup ^= i
        if a & lsb:
            miss_or_dup ^= a
    if miss_or_dup in A:
        duplicate = miss_or_dup
        missing = duplicate ^ miss_xor_dup
    else:
        missing = miss_or_dup
        duplicate = miss_xor_dup ^ missing
    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
