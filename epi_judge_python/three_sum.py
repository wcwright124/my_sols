from test_framework import generic_test


def has_three_sum(A, t):
    # TODO - you fill in here.
    A.sort()
    for i in range(len(A)):
        left, right = i, len(A) - 1
        required_sum = t - A[i]
        while left <= right:
            if A[left] + A[right] == required_sum:
                return True
            elif A[left] + A[right] < required_sum:
                left += 1
            else:
                right -= 1 
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
