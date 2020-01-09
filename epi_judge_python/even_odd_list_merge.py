from test_framework import generic_test


def even_odd_merge(L):
    # TODO - you fill in here.
    if not L:
        return L
    new_head, odd_head = L, L.next
    even, odd = L, L.next
    is_even = True
    while even and odd:
        if is_even:
            even.next = odd.next
            if even.next:
                even = even.next
            else:
                break
        else:
            odd.next = even.next
            odd = odd.next
        is_even = not is_even
    even.next = odd_head
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
