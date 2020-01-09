from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    dummy = ListNode(-1, L)
    lag, lead = dummy, L
    for _ in range(k):
        lead = lead.next
    while lead:
        lag, lead = lag.next, lead.next
    lag.next = lag.next.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
