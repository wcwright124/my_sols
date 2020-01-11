import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A, k):
    # TODO - you fill in here.
    if not A or k <= 0:
        return []
    max_heap = [(-A[0], 0)]
    res = []
    for _ in range(k):
        val, idx = heapq.heappop(max_heap)
        if 2 * idx + 1 < len(A):
            heapq.heappush(max_heap, (-A[2 * idx + 1], 2 * idx + 1))
        if 2 * idx + 2 < len(A):
            heapq.heappush(max_heap, (-A[2 * idx + 2], 2 * idx + 2))
        res.append(-val)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
