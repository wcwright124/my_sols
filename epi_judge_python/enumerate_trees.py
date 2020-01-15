import bintrees
import copy
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def generate_all_binary_trees(num_nodes):
    def helper(n):
        if n == 0:
            results.append([None])
            return
        helper(n - 1)
        res = []
        root = BSTNode(n)
        for i in range(n):
            left = results[i]
            right = results[n-1-i]
            for left_root in left:
                for right_root in right:
                    temp_root = copy.copy(root)
                    temp_root.left = left_root
                    temp_root.right = right_root
                    res.append(temp_root)
        results.append(res)
        return 
    # TODO - you fill in here.
    results = []
    helper(num_nodes)
    return results[-1]


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_trees.py",
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
