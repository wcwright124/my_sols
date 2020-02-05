import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def bst_to_doubly_linked_list(tree):
    # TODO - you fill in here.
    def helper(node):
        if not node:
            return (None, None)
        left_head, left_tail = helper(node.left)
        right_head, right_tail = helper(node.right)
        if left_tail:
            left_tail.right = node
        node.left = left_tail
        if right_head:
            right_head.left = node
        node.right = right_head
        new_head = left_head or node
        new_tail = right_tail or node
        return new_head, new_tail
    head, _ = helper(tree)
    return head


@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_to_sorted_list.py",
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
