from test_framework import generic_test

def num_combinations_for_final_score(final_score, individual_play_scores): # O(nk) time | O(n) space
    n = final_score
    k = len(individual_play_scores)
    dp_odd = [0] * (n + 1)
    dp_even = [0] * (n + 1)
    dp_odd[0], dp_even[0] = 1, 1
    
    for i in range(k):
        if i % 2 == 1:
            prev = dp_even
            curr = dp_odd
        else:
            prev = dp_odd
            curr = dp_even
        
        val = individual_play_scores[i]
        for j in range(1, n + 1):
            curr[j] = prev[j]
            if j - val >= 0:
                curr[j] += curr[j - val]
    return curr[-1]


def num_combinations_for_final_score2(final_score, individual_play_scores): # O(nk) time | O(nk) space
    # TODO - you fill in here.
    n = final_score
    k = len(individual_play_scores)
    dp = [[0] * (n + 1)] * k
    
    for i in range(k):
        dp[i][0] = 1

    for j in range(1, n + 1):
        val = individual_play_scores[0]
        if j - val >= 0:
            dp[0][j] += dp[0][j - val]
    
    for i in range(1, k):
        for j in range(1, n + 1):
            val = individual_play_scores[i]
            dp[i][j] = dp[i - 1][j]
            if j - val >= 0:
                dp[i][j] += dp[i][j - val]

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
