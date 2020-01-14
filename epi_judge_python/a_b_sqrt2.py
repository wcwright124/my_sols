import bintrees
import heapq
import math

from test_framework import generic_test

class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + math.sqrt(2) * b
    
    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

def generate_first_k_a_b_sqrt2_slow(k): # O(k log k) time | O(k log k) space
    res = set()
    heap = [Number(0,0)]
    while len(res) < k:
        curr = heapq.heappop(heap)
        if curr.val not in res:
            res.add(curr.val)
            x, y = Number(curr.a+1, curr.b), Number(curr.a, curr.b+1)
            heapq.heappush(heap, x)
            heapq.heappush(heap, y)
    res = list(res)
    res.sort()
    return res






def generate_first_k_a_b_sqrt2_slow2(k): # O(k log k) time | O(k log k) space
    # TODO - you fill in here.
    res = []
    candidates = bintrees.RBTree()
    candidates[Number(0, 0)] = None
    while len(res) < k:
        curr = candidates.pop_min()[0]
        res.append(curr.val)
        candidates[Number(curr.a + 1, curr.b)] = None
        candidates[Number(curr.a, curr.b + 1)] = None
    return res

def generate_first_k_a_b_sqrt2(k): # O(k) time | O(k) space
    res = [Number(0,0)]
    i, j = 0, 0
    for _ in range(1, k):
        cand_i_plus_1 = Number(res[i].a + 1, res[i].b)
        cand_j_plus_root2 = Number(res[j].a, res[j].b + 1)
        res.append(min(cand_i_plus_1, cand_j_plus_root2))
        if cand_i_plus_1 == res[-1]:
            i += 1
        if cand_j_plus_root2 == res[-1]:
            j += 1
    return [r.val for r in res]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2_slow))
