import functools
from test_framework import generic_test


def rabin_karp(text, search):
    # TODO - you fill in here.
    if len(search) > len(text):
        return -1
    
    NUM_CHARS = 26
    text_hash = functools.reduce(lambda h, c: h * NUM_CHARS + ord(c), text[:len(search)], 0)
    search_hash = functools.reduce(lambda h, c: h * NUM_CHARS + ord(c), search, 0)
    power_search = NUM_CHARS ** max(len(search) - 1, 0)
    
    for i in range(len(search), len(text)):
        if text_hash == search_hash and text[i-len(search): i] == search:
            return i - len(search)
        
        text_hash -= ord(text[i - len(search)]) * power_search
        text_hash = NUM_CHARS * text_hash + ord(text[i])
    
    if text_hash == search_hash and text[-len(search):] == search:
        return len(text) - len(search)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
