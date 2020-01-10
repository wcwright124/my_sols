import collections

from test_framework import generic_test


def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree:
        return []
    res = []
    node_queue = collections.deque()
    node_queue.append(tree)
    while node_queue:
        row = []
        for _ in range(len(node_queue)):
            node = node_queue.popleft()
            row.append(node.data)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)
        res.append(row)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
