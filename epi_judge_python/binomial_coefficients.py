import functools

from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    @functools.lru_cache(None)
    def binomial_helper(n, k):
        if n < k:
            return 0
        if n == k or k == 0:
            return 1
        return binomial_helper(n-1, k) + binomial_helper(n-1, k-1)
    # TODO - you fill in here.
    return binomial_helper(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
