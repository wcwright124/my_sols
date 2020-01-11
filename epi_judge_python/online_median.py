import heapq

from test_framework import generic_test


def online_median(sequence):
    def balance():
        if len(right_heap) > len(left_heap) + 1:
            val = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -val)
        elif len(left_heap) > len(right_heap):
            val = heapq.heappop(left_heap)
            heapq.heappush(right_heap, -val)
    # TODO - you fill in here.
    left_heap, right_heap = [], []
    num_elts = 0
    res = []
    for s in sequence:
        num_elts += 1
        if not right_heap:
            heapq.heappush(right_heap, s)
        else:
            last_median = res[-1]
            if s >= last_median:
                heapq.heappush(right_heap, s)
            else:
                heapq.heappush(left_heap, -s)
            balance()
        if num_elts % 2 == 1:
            res.append(right_heap[0])
        else:
            new_median = (right_heap[0] - left_heap[0]) / 2
            res.append(new_median)
    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
