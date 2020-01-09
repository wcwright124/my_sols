import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def list_pivoting(l, x):
    # TODO - you fill in here.
    if not l:
        return l
    smaller, equal, bigger = ListNode(0, l), ListNode(0, l), ListNode(0, l)
    nodes = [smaller, equal, bigger]
    curr = l
    while curr:
        if curr.data < x:
            idx = 0
        elif curr.data == x:
            idx = 1
        else:
            idx = 2
        nodes[idx].next = curr
        curr = curr.next
        nodes[idx] = nodes[idx].next
    # logic to connect things in correct order
    nodes[2].next = None
    nodes[1].next = bigger.next
    nodes[0].next = equal.next
    return smaller.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
