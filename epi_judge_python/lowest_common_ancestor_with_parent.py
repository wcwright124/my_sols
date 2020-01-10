import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def depth(node):
        depth = -1
        while node:
            node = node.parent
            depth += 1
        return depth
    # TODO - you fill in here.
    depth0 = depth(node0)
    depth1 = depth(node1)
    if depth0 > depth1:
        for _ in range(depth0 - depth1):
            node0 = node0.parent
    else:
        for _ in range(depth1 - depth0):
            node1 = node1.parent
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
