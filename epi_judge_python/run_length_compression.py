from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    # TODO - you fill in here.
    res = []
    i, j = 0, 0
    while j < len(s):
        while j < len(s) and s[j].isnumeric():
            j += 1
        count = int(s[i:j])
        char = s[j]
        res.append(char * count)
        j += 1
        i = j
    return ''.join(res)


def encoding(s):
    # TODO - you fill in here.
    res = []
    i, j = 0, 0
    while j < len(s):
        while j < len(s) and s[i] == s[j]:
            j += 1
        res.append(str(j-i))
        res.append(s[i])
        i = j
    return ''.join(res)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
