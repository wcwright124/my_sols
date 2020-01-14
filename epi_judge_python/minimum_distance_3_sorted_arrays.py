import bintrees
import heapq

from test_framework import generic_test

def find_closest_elements_in_sorted_arrays(sorted_arrays):
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)
    
    min_so_far = float('inf')
    while True:
        min_val, min_idx = iters.min_key()
        max_val = iters.max_key()[0]
        min_so_far = min(min_so_far, max_val - min_val)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return int(min_so_far)
        iters.insert((next_min, min_idx), it)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
