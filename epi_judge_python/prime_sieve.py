import math

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    # TODO - you fill in here.
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*p, n + 1, p):
                is_prime[i] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
