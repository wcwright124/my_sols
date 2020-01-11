import heapq

from test_framework import generic_test

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ")"

def reverse_decreasing_subarrays(A, intervals):
    for interval in intervals:
        start = interval.start
        end = interval.end
        if A[start] > A[end-1]:
            A[start:end] = list(reversed(A[start:end]))
    return A

def get_monotone_subarrays(A):
    crit_pts = [0]
    for i, a in enumerate(A):
        if 0 < i < len(A) - 1:
            if (a > A[i-1]) and (a >= A[i+1]):
                crit_pts.append(i)
            elif (a <= A[i-1]) and (a < A[i+1]):
                crit_pts.append(i)
    crit_pts.append(len(A))
    res = [Interval(crit_pts[i], crit_pts[i+1]) for i in range(len(crit_pts)-1)]
    return res

def sort_k_increasing_decreasing_array(A):
    # TODO - you fill in here.
    res = []
    intervals = get_monotone_subarrays(A)
    A = reverse_decreasing_subarrays(A, intervals)
    min_heap = [(A[interval.start], interval.start, interval.end) for interval in intervals]
    heapq.heapify(min_heap)
    while min_heap:
        val, start_idx, end_idx = heapq.heappop(min_heap)
        res.append(val)
        start_idx += 1
        if start_idx < end_idx:
            new_val = A[start_idx]
            heapq.heappush(min_heap, (new_val, start_idx, end_idx))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
