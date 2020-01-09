from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def remove_duplicates(L):
    # TODO - you fill in here.
    dummy = ListNode(0, L)
    curr = L
    while curr and curr.next:
        while curr and curr.next and curr.next.data == curr.data:
            curr.next = curr.next.next
        if curr:
            curr = curr.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
