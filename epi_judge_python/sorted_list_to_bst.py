import functools

from doubly_list_node import DoublyListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def find_mid(head):
    if not head:
        return None
    lead, lag = head, head
    while lead and lead.next:
        lead, lag = lead.next.next, lag.next
    return lag
# Returns the root of the corresponding BST. The prev and next fields of the
# list nodes are used as the BST nodes left and right fields, respectively.
# The length of the list is given.
def build_bst_from_sorted_doubly_list(l, n):
    # TODO - you fill in here.
    def build_bst_helper(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        left = build_bst_helper(start, mid)
        curr, head[0] = head[0], head[0].next
        curr.prev = left
        curr.next = build_bst_helper(mid + 1, end)
        return curr
    head = [l]
    return build_bst_helper(0, n)
    
def build_bst_from_sorted_doubly_list1(l, n):
    def helper(node):
        if not node:
            return None
        root = find_mid(node)
        left_head = node if node is not root else None
        root.prev, root.prev.next = None, None
        right_head = root.next
        root.prev = root.next = None
        root.prev = helper(left_head)
        root.next = helper(right_head)
        return root
    return helper(l)


def compare_vector_and_tree(tree, it):
    if not tree:
        return

    compare_vector_and_tree(tree.prev, it)

    v = next(it, None)
    if v is None:
        raise TestFailure("Too few values in the tree")
    if v != tree.data:
        raise TestFailure("Unexpected value")

    compare_vector_and_tree(tree.next, it)


@enable_executor_hook
def build_bst_from_sorted_doubly_list_wrapper(executor, l):
    input_list = None
    for v in reversed(l):
        input_list = DoublyListNode(v, next=input_list)
        if input_list.next != None:
            input_list.next.prev = input_list

    input_list = executor.run(
        functools.partial(build_bst_from_sorted_doubly_list, input_list,
                          len(l)))

    it = iter(l)
    compare_vector_and_tree(input_list, it)
    if next(it, None) is not None:
        raise TestFailure("Too many l in the tree")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sorted_list_to_bst.py", "sorted_list_to_bst.tsv",
            build_bst_from_sorted_doubly_list_wrapper))
