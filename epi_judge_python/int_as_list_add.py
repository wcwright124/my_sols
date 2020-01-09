from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def add_two_numbers(L1, L2):
    # TODO - you fill in here.
    # Using ternary ops cuts down on code length. do this in future
    dummy = ListNode()
    curr = dummy
    carry = 0
    while L1 or L2 or carry:
        temp = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        curr.next = ListNode(temp % 10)
        curr = curr.next
        carry = temp // 10
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
