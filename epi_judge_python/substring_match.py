import functools
from test_framework import generic_test


def knuth_morris_pratt(string, substring):
    def buildPattern():
        pattern = [-1 for _ in substring]
        i, j = 0, 1
        while j < len(substring):
            if substring[j] == substring[i]:
                pattern[j] = i
                i += 1
                j += 1
            elif i > 0:
                i = pattern[i-1] + 1
            else:
                j += 1
        return pattern
    if len(substring) > len(string):
	    return -1
    if len(substring) == 0:
        return 0
    patternTable = buildPattern()
    string_idx = 0
    substring_idx = 0
    while string_idx < len(string):
        if substring[substring_idx] == string[string_idx]:
            substring_idx += 1
            string_idx += 1
        elif substring_idx > 0:
            substring_idx = patternTable[substring_idx-1] + 1
        else:
            string_idx += 1
        if substring_idx == len(substring):
            return string_idx-len(substring)
    return -1

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
                                       'substring_match.tsv', knuth_morris_pratt))
