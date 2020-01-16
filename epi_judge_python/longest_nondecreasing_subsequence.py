from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    # TODO - you fill in here.
    if not A:
        return 0
    max_length = 1
    dp = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] <= A[i]:
                dp[i] = max(dp[i], 1 + dp[j])
        max_length = max(max_length, dp[i])
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
