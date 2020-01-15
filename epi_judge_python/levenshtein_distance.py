import functools

from test_framework import generic_test


def levenshtein_distance(A: str, B:str) -> int:
    @functools.lru_cache(None)
    def levenhstein_helper(idx_A, idx_B):
        if idx_A < 0:
            return idx_B + 1
        if idx_B < 0:
            return idx_A + 1
        if A[idx_A] == B[idx_B]:
            return levenhstein_helper(idx_A - 1, idx_B - 1)
        substitute = levenhstein_helper(idx_A - 1, idx_B - 1)
        add = levenhstein_helper(idx_A, idx_B - 1)
        remove = levenhstein_helper(idx_A - 1, idx_B)
        return 1 + min(substitute, min(add, remove))
    return levenhstein_helper(len(A)-1, len(B)-1)


def levenshtein_distance2(A, B): # O(mn) time | O (min(m,n)) space
    if len(B) < len(A):
        A, B = B, A
    
    dp_o = [0 for _ in range(len(A) + 1)]
    dp_e = [x for x in range(len(A) + 1)]
    
    for i in range(1, len(B) + 1):
        if i % 2 == 0:
            prev, curr = dp_o, dp_e
        else:
            prev, curr = dp_e, dp_o
        
        curr[0] = 1 + prev[0]
        for j in range(1, len(A) + 1):
            if B[i-1] == A[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(curr[j-1], min(prev[j-1], prev[j]))

    return curr[-1]

def levenshtein_distance1(A, B): # O(nm) time | O(nm) space
    # TODO - you fill in here.
    dp = [[0 for _ in range(len(A) + 1)] for _ in  range(len(B) + 1)]

    for i in range(1, len(B) + 1):
        dp[i][0] = i
    for j in range(1, len(A) + 1):
        dp[0][j] = j
    
    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i-1] == A[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))

    return dp[-1][-1]


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
