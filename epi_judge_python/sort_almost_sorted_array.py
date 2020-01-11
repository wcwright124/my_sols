import heapq

from test_framework import generic_test


def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    min_heap = []
    res = []
    for s in sequence:
        if len(min_heap) < k:
            heapq.heappush(min_heap, s)
        else:
            res.append(heapq.heappushpop(min_heap, s))
    for _ in range(k):
        res.append(heapq.heappop(min_heap))
    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
