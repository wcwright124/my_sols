from test_framework import generic_test


def next_permutation(perm):
    # TODO - you fill in here.
    i = len(perm) - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1
    i -= 1
    if i == -1: # last permutation possible
        return []
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    perm[i], perm[j] = perm[j], perm[i]
    perm[i+1:] = reversed(perm[i+1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
