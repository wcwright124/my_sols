from test_framework import generic_test


def ss_decode_col_id(col): # O(n) time | O(1) space
    # TODO - you fill in here.
    if not col:
        return 0
    res = 0
    for c in col:
        res = 26 * res + 1 + ord(c) - ord('A')
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
    
