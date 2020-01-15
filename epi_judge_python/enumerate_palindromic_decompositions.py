from test_framework import generic_test

def is_palindromic_substring(s, i, j):
    if i > j:
        raise ValueError('j must be greater than or equal to i')
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def palindrome_decompositions(s):
    def helper(start, partial):
        if start == n:
            res.append(partial)
            return
        for i in range(start, n):
            if is_palindromic_substring(s, start, i):
                helper(i+1, partial + [s[start:i+1]])
        return
    # TODO - you fill in here.
    res = []
    n = len(s)
    helper(0, [])
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
