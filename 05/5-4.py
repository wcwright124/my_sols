"""
Write a program to compute the minimum number of steps needed to advance to the last location
"""

def min_steps(arr):
    # dp[i] gives minimum number of steps needed to reach index i
    dp = [float('inf')] * len(arr)
    dp[0] = 0
    for i in range(len(arr)):
        jumps = arr[i]
        for j in range(i, min(i + jumps + 1, len(arr))):
            dp[j] = min(dp[j], 1 + dp[i])
    return dp[-1]

if __name__ == '__main__':
    a1 = [3,3,1,0,2,0,1]
    a2 = [3,2,0,0,2,0,1]
    a3 = [2,4,1,1,0,2,3]
    a4 = [3,3,1,0,2,0,1]
    a5 = [3,2,0,0,2,0,1]
    tests = [a1, a2, a3, a4, a5]
    for t in tests:
        print(min_steps(t))