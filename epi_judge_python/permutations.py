from test_framework import generic_test, test_utils


def permutations(A):
    def helper(idx):
        if idx == len(A) - 1:
            res.append(A[:])
        else:
            for i in range(idx, len(A)):
                A[idx], A[i] = A[i], A[idx]
                helper(idx + 1)
                A[i], A[idx] = A[idx], A[i]

    # TODO - you fill in here.
    res = []
    helper(0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
