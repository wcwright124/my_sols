from test_framework import generic_test, test_utils

def combinations(n, k):
    def helper(offset, combo):
        if len(combo) == k:
            res.append(combo[:])
            return
        num_remaining = k - len(combo)
        for x in range(offset, n - num_remaining + 2):
            helper(x + 1, combo + [x])
        return
    if k == 0:
        return [[]]
    res = []
    helper(1, [])
    return res

def combinations1(n, k):
    def helper(n, k, curr_combo):
        if k == 0 and n >= 0:
            res.append(curr_combo)
            return
        elif n < 0:
            return 
        else:
            for i in range(n, k - 1, -1):
                helper(i - 1, k - 1, curr_combo + [i])
            return 
    res = []
    helper(n, k, [])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
