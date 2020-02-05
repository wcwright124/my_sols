from test_framework import generic_test

# Cleaner implementation from EPI
def justify_text(words, L):
    curr_line_len, res = 0, []
    curr_line = []
    for word in words:
        if curr_line_len + len(word) + len(curr_line) > L:
            for i in range(L- curr_line_len):
                curr_line[i % max(len(curr_line) - 1, 1)] += ' '
            res.append(''.join(curr_line))
            curr_line, curr_line_len = [], 0
        curr_line.append(word)
        curr_line_len += len(word)
    return res + [' '.join(curr_line).ljust(L)]

def justify_text1(words, L):
    # TODO - you fill in here.
    i = 0
    res = []
    while i < len(words):
        curr_row = []
        chars_used = 0
        while i < len(words) and chars_used + len(curr_row) + len(words[i]) <= L:
            curr_row.append(words[i])
            chars_used += len(words[i])
            i += 1
        if i == len(words):
            while chars_used + len(curr_row) <= L:
                curr_row[-1] = curr_row[-1] + ' '
                chars_used += 1
            res.append(' '.join(curr_row))
            break
        j = 0
        while chars_used < L:
            curr_row[j] = curr_row[j] + ' '
            chars_used += 1
            j = (j + 1) % max(1, len(curr_row) - 1)
        res.append(''.join(curr_row))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))
