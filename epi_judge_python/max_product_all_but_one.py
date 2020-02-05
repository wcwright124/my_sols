import functools

from test_framework import generic_test


def find_biggest_n_minus_one_product(A):
    # TODO - you fill in here.
    num_neg = 0
    least_neg_idx = least_nonneg_idx = greatest_neg_idx = None
    for i, a in enumerate(A):
        if a < 0:
            num_neg += 1
            if (least_neg_idx is None) or (a > A[least_neg_idx]):
                least_neg_idx = i
            if (greatest_neg_idx is None) or (a < A[greatest_neg_idx]):
                greatest_neg_idx = i
        else:
            if (least_nonneg_idx is None) or (a < A[least_nonneg_idx]):
                least_nonneg_idx = i
    # compute skip_idx based on above
    skip_idx = -1
    if num_neg % 2 == 0:
        skip_idx = least_nonneg_idx
    else:
        skip_idx = greatest_neg_idx if num_neg == len(A) else least_neg_idx
    return functools.reduce(lambda prod, a: prod * a, (a for i, a in enumerate(A) if i != skip_idx), 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_product_all_but_one.py",
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
