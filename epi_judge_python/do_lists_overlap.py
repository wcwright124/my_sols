import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0, l1):
    def length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def get_cycle_length(head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = fast.next
                length = 1
                while fast is not slow:
                    fast = fast.next
                    length += 1
                return length, slow
        return -1, None
    
    l0_cycle_len, node0 = get_cycle_length(l0)
    l1_cycle_len, node1 = get_cycle_length(l1)
    if l0_cycle_len > 0 and l1_cycle_len > 0: # both have cycles
        if l0_cycle_len != l1_cycle_len:
            return None
        for _ in range(l0_cycle_len):
            if node0 is node1:
                return node0
            node0 = node0.next
        return None
    elif l0_cycle_len > 0 or l1_cycle_len > 0: # can't intersect
        return None
    else: # neither contains a cycle
        # follow logic from problem 7.4
        n0, n1 = length(l0), length(l1)
        if n0 < n1:
            for _ in range(n1-n0):
                l1 = l1.next
        else:
            for _ in range(n0 - n1):
                l0 = l0.next
        while l0 is not l1:
            l0, l1 = l0.next, l1.next
        return l0
    return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
