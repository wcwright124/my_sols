from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def cyclically_right_shift_list(L, k):
    def length(head):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        return length
    # TODO - you fill in here.
    if not L:
        return L
    length = length(L)
    k = k % length
    if k == 0:
        return L
    
    dummy = ListNode(0, L)
    lag, lead = L, L
    for _ in range(k - 1):
        lead = lead.next
    prev = dummy
    while lead.next:
        prev, lag, lead = prev.next, lag.next, lead.next
    new_head = lag
    prev.next = None
    lead.next = dummy.next
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
