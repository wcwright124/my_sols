from test_framework import generic_test

def find_first_missing_positive(A):
    # TODO - you fill in here.
    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
            j = A[i] - 1
            A[i], A[j] = A[j], A[i]
    
    for i, a in enumerate(A, 1):
        if a != i:
            return i
    
    return len(A) + 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("first_missing_positive_entry.py",
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
