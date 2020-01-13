from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def stable_sort_list(L):
    def merge(head1, head2):
        dummy = ListNode()
        curr = dummy
        while head1 and head2:
            if head1.data <= head2.data:
                temp = head1.next
                curr.next = head1
                head1.next = None
                head1 = temp
                curr = curr.next
            else:
                temp = head2.next
                curr.next = head2
                head2.next = None
                head2 = temp
                curr = curr.next
        if head1:
            curr.next = head1
        elif head2:
            curr.next = head2
        return dummy.next
    # TODO - you fill in here.
    if (not L) or (not L.next):
        return L
    
    # get mid point
    fast, slow, pre_slow = L, L, None
    while fast and fast.next:
        pre_slow, slow, fast = slow, slow.next, fast.next.next
    
    if pre_slow:
        pre_slow.next = None

    return merge(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
