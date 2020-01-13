import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    key_to_idx = {k: i for i, k in enumerate(keywords)}
    last_obs_idx = [-1] * len(keywords)
    
    # For each keyword (identified by its index in keywords array), the length
    # of the shortest subarray ending at the most recent occurrence of that
    # keyword that sequentially cover all keywords up to that keyword.
    shortest_sub_length = [float('inf')] * len(keywords)

    shortest_distance = float('inf')
    start, end = -1, -1
    for i, p in enumerate(paragraph):
        if p in key_to_idx:
            key_idx = key_to_idx[p]
            if key_idx == 0:  # First keyword.
                shortest_sub_length[key_idx] = 1
            elif shortest_sub_length[key_idx - 1] != float('inf'):
                dist_to_last_key = i - last_obs_idx[key_idx - 1]
                shortest_sub_length[key_idx] = dist_to_last_key + shortest_sub_length[key_idx - 1]
            last_obs_idx[key_idx] = i

            # Last keyword, for improved subarray.
            if key_idx == len(keywords) - 1 and shortest_sub_length[-1] < shortest_distance:
                shortest_distance = shortest_sub_length[-1]
                start, end = i - shortest_distance + 1, i
    return Subarray(start, end)


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
