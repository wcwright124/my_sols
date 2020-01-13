import heapq
import random

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def pivot(start, end, piv_idx):
        pivot_val = A[piv_idx]
        A[piv_idx], A[end] = A[end], A[piv_idx]
        curr_piv_idx = start
        for i in range(start, end):
            if A[i] > pivot_val:
                A[i], A[curr_piv_idx] = A[curr_piv_idx], A[i]
                curr_piv_idx += 1
        A[end], A[curr_piv_idx] = A[curr_piv_idx], A[end]
        return curr_piv_idx
    # TODO - you fill in here.
    if k > len(A) or len(A) == 0:
        return
    start_idx, end_idx = 0, len(A) - 1
    piv_idx = -1
    while start_idx <= end_idx:
        piv_idx = random.randint(start_idx, end_idx)
        idx = pivot(start_idx, end_idx, piv_idx)
        if idx == k - 1:
            return A[idx]
        elif idx > k - 1:
            end_idx = idx - 1
        else:
            start_idx = idx + 1
    return 0

def find_kth_largest_heap(k, A): # O(n log k) time | O(k) space
    min_heap = A[:k]
    heapq.heapify(min_heap)
    for i in range(k, len(A)):
        if A[i] > min_heap[0]:
            heapq.heappushpop(min_heap, A[i])
    return min_heap[0]


def find_kth_largest_bf(k, A): # O(n log n) time | O(n) space
    A.sort() # timsort
    return A[-k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
