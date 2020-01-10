from test_framework import generic_test


def is_well_formed(s):
    # TODO - you fill in here.
    stack = []
    OPEN_CHARS = ['(', '[', '{']
    CLOSE_CHARS = [')', ']', '}']
    match = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in CLOSE_CHARS:
            if not stack:
                return False
            elif stack.pop() != char:
                return False
        elif char in OPEN_CHARS:
            # add corresponding close char to stack
            stack.append(match[char])
        else: # input string was invalid
            return False
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
