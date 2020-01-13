import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    # TODO - you fill in here.
    keys_to_idx = {k:i for i, k in enumerate(keywords)}
    last_key_idx = [-1] * len(keywords) # idx of last occurence of keyword i
    
    # keeps track of length of smallest subarray containing all keys up to and
    # including keywords[i]. At the end of the run the last entry will be the
    # length of the smallest subarray containing all keywords sequentially
    smallest_sub_length = [float('inf')] * len(keywords)
   
    shortest_dist = float('inf')
    start, end = -1, -1
    for i, word in enumerate(paragraph):
        if word in keys_to_idx:
            key_idx = keys_to_idx[word] 
            if key_idx == 0:
                last_key_idx[0] = i
                smallest_sub_length[0] = 1
            elif smallest_sub_length[key_idx] != float('inf'):
                last_key_idx[key_idx] = i
                dist_to_last_key = i - last_key_idx[key_idx - 1]
                curr_sub_length = dist_to_last_key + smallest_sub_length[key_idx - 1]
                smallest_sub_length[key_idx] = min(smallest_sub_length[key_idx], curr_sub_length)
            if key_idx == len(keywords) - 1 and smallest_sub_length[-1] < shortest_dist:
                shortest_dist = smallest_sub_length[-1]
                start, end = i - shortest_dist + 1, i
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
