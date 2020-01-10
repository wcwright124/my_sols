import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca2(tree, node0, node1):
    def helper(node):
        if not node:
            return None
        left = helper(node.left)
        right = helper(node.right)
        if left and right:
            return node
        elif left:
            if (node is node0) or (node is node1):
                return node
            return left
        elif right:
            if (node is node0) or (node is node1):
                return node
            return right
        else:
            if node is node0:
                return node
            if node is node1:
                return node
            return None
    return helper(tree)

def lca(tree, node0, node1):
    # TODO - you fill in here.
    def helper(node):
        if not node:
            return None, 0
        left_lca, left_node_count = helper(node.left)
        if left_node_count == 2:
            return left_lca, 2
        right_lca, right_node_count = helper(node.right)
        if right_node_count == 2:
            return right_lca, 2
        node_count = left_node_count + right_node_count
        if node is node0:
            node_count += 1
        if node is node1:
            node_count += 1
        return node, node_count
    lca, _ = helper(tree)
    return lca


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
