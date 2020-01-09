from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    def reverse_after(head):
        prev, curr = head, head.next
        prev.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    # TODO - you fill in here.
    if not L:
        return True
    
    lag, lead = L, L
    while lead and lead.next:
        lag, lead = lag.next, lead.next.next
    # lag is middle node (if oddd), one plus if even
    left = L
    right = reverse_after(lag)
    while left and right:
        if left.data != right.data:
            return False
        left, right = left.next, right.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
