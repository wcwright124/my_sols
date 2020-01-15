import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def knapsack_helper(i, curr_capacity):
        #if curr_capacity <= 0:
        #    return 0
        if i < 0:
            return 0
        #if i == 0:
        #    return items[0].value if curr_capacity >= items[0].weight else 0
        
        exclude = knapsack_helper(i-1, curr_capacity)
        include = 0 if curr_capacity < items[i].weight else items[i].value + knapsack_helper(i-1, curr_capacity - items[i].weight)
        return max(include, exclude) 
    return knapsack_helper(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
