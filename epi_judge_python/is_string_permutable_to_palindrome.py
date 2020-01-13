import collections

from test_framework import generic_test

def can_form_palindrome_one_line(s):
    return sum(v%2 for v in collections.Counter(s).values()) <= 1

def can_form_palindrome(s):
    # TODO - you fill in here.
    num_odd_char_counts = 0
    char_counts = collections.Counter(s)
    for count in char_counts.values():
        if count % 2 != 0:
            num_odd_char_counts += 1
            if num_odd_char_counts > 1:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
