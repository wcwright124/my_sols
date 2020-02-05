import heapq
import random

from test_framework import generic_test

def kth_largest(arr, k):
    def partition(lo, hi, piv_idx):
        piv_val = arr[piv_idx]
        arr[piv_idx], arr[hi] = arr[hi], arr[piv_idx]
        new_piv_idx = lo
        for i in range(lo, hi):
            if arr[i] > piv_val:
                arr[i], arr[new_piv_idx] = arr[new_piv_idx], arr[i]
                new_piv_idx += 1            
        arr[hi], arr[new_piv_idx] = arr[new_piv_idx], arr[hi]
        return new_piv_idx
    
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        piv_idx = random.randint(lo, hi)
        new_piv_idx = partition(lo, hi, piv_idx)
        if new_piv_idx == k - 1:
            return arr[new_piv_idx]
        elif new_piv_idx > k - 1:
            hi = new_piv_idx - 1
        else:
            lo = new_piv_idx + 1
    return arr[new_piv_idx]


def find_kth_largest_unknown_length(stream, k):
    # TODO - you fill in here.
    candidates = []
    for x in stream:
        candidates.append(x)
        if len(candidates) >= 2 * k - 1:
            kth_largest(candidates, k)
            del candidates[k:]
    return kth_largest(candidates, k)


# Pythonic solution that uses library method but costs O(n log k) time.
def find_kth_largest_unknown_length_pythonic(stream, k):
    return heapq.nlargest(k, stream)[-1]


def find_kth_largest_unknown_length_wrapper(stream, k):
    return find_kth_largest_unknown_length(iter(stream), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "kth_largest_element_in_long_array.py",
            'kth_largest_element_in_long_array.tsv',
            find_kth_largest_unknown_length_wrapper))
