from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    carry = 1
    for i in range(len(A) - 1, -1, -1):
        temp = A[i] + carry
        A[i] = temp % 10
        carry = temp // 10
    if carry:
        A = [1] + A
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
