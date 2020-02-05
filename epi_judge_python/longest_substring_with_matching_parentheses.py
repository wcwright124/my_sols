from test_framework import generic_test


def longest_matching_parentheses(s): # O(n) time | O(n)
    # TODO - you fill in here.
    max_match_len = 0
    stack = []
    match_start = -1
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif len(stack) == 0:
            match_start = i
        else:
            stack.pop()
            left = stack[-1] if stack else match_start
            max_match_len = max(max_match_len, i - left)
    return max_match_len


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_substring_with_matching_parentheses.py",
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
