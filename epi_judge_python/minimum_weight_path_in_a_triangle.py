from test_framework import generic_test


def minimum_path_weight(triangle):
    # TODO - you fill in here.
    if not triangle:
        return 0
    dp = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        dp_row = [triangle[i][0] + dp[i-1][0]]
        for j in range(1, len(triangle[i]) - 1):
            dp_row.append(triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j]))
        dp_row.append(triangle[i][-1] + dp[i-1][-1])
        dp.append(dp_row)
    return min(dp[-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
