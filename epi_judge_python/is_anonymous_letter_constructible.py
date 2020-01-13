import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here
    letter_char_counts = collections.Counter(letter_text)
    for char in magazine_text:
        if char in letter_char_counts:
            letter_char_counts[char] -= 1
            if letter_char_counts[char] == 0:
                del letter_char_counts[char]
            if len(letter_char_counts) == 0:
                return True
    return len(letter_char_counts) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
