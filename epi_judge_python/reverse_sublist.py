from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    if not L:
        return L
    
    dummy = ListNode(-1, L)
    
    prev, curr = dummy, L
    for _ in range(start-1):
        prev, curr = curr, curr.next
    node_before_reverse = prev
    sublist_start_node = curr
    prev, curr = curr, curr.next
    # reverse logic
    for _ in range(finish - start):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    node_before_reverse.next = prev
    sublist_start_node.next = curr
    
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
