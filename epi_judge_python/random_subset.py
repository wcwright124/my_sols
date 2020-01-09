import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

def random_subset1(n, k): # O(n) time | O(n) space
    res = list(range(n))
    for i in range(k):
        j = random.randint(i, n-1)
        res[i], res[j] = res[j], res[i]
    return res[:k]

def random_subset2(n, k): # O(k logk) time | O(k) space
    res = []
    already_drawn = set()
    for _ in range(k):
        x = random.randint(0, n-1)
        while x in already_drawn:
            x = random.randint(0, n-1)
        res.append(x)
        already_drawn.add(x)
    return res

def random_subset(n, k): # O(k) time | O(k) space
    permuted = {}
    for i in range(k):
        j = random.randint(i, n-1)
        perm_j = permuted.get(j, j)
        perm_i = permuted.get(i, i)
        permuted[i] = perm_j
        permuted[j] = perm_i
    return [permuted[i] for i in range(k)]

    



@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("random_subset.py", 'random_subset.tsv',
                                       random_subset_wrapper))
