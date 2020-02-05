from test_framework import generic_test


def zipping_linked_list(L):
    # TODO - you fill in here.
    if (not L) or (not L.next):
        return L
    
    # find middle of list (or left center if even length)
    lead, lag = L, L
    while lead.next and lead.next.next:
        lag, lead = lag.next, lead.next.next
    
    # reverse second half
    prev, curr = None, lag.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    # disconnect left half and right half
    lag.next = None
    
    # merge left and right half
    right = prev
    left = L
    head = L
    while left and right:
        next_left = left.next
        next_right = right.next
        left.next = right
        right.next = next_left
        left, right = next_left, next_right
    
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
