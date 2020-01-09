from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = conversion[s[-1]]
    for i in range(len(s)-2, -1, -1):
        if conversion[s[i]] < conversion[s[i+1]]:
            res -= conversion[s[i]]
        else:
            res += conversion[s[i]]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
