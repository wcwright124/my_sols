import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def reconstruct_preorder(preorder):
    # TODO - you fill in here.
    def helper():
        root_val = next(pre_iter)
        if root_val is None:
            return None
        root = BinaryTreeNode(root_val)
        root.left = helper()
        root.right = helper()
        return root
    pre_iter = iter(preorder)
    return helper()


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
