from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    if not A:
        return 0
    previous_entries = set()
    i = 0
    res = 1
    for j, a in enumerate(A):
        if a in previous_entries:
            while A[i] != a:
                previous_entries.remove(A[i])
                i += 1
            i += 1
        else:
            previous_entries.add(a)
        res = max(res, j - i + 1)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
