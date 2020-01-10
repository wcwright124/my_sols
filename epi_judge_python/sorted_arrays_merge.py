import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays): # O(N log k) time | O(N + k) space where N = sum of lengths of arrays
    # TODO - you fill in here.
    res = []
    min_heap = [(arr[0], idx, 0) for idx, arr in enumerate(sorted_arrays)]
    heapq.heapify(min_heap)
    while min_heap:
        val, arr_idx, val_idx = heapq.heappop(min_heap)
        res.append(val)
        val_idx += 1
        if val_idx < len(sorted_arrays[arr_idx]):
            new_val = sorted_arrays[arr_idx][val_idx]
            heapq.heappush(min_heap, (new_val, arr_idx, val_idx))
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
