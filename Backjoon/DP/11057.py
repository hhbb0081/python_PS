# 11057 오르막수

import sys
input = sys.stdin.readline

n = int(input())

# 1 -> 0 1 2 3 4 5 6 7 8 9
# 2 -> 00 / 01 11 / 02 12 22 / 03 13 23 33 / 04 14 24 34 44 / ...
# 3 -> 000 / 001 011 111 / 002 012 112 022 122 222 /
# 4 -> 0000 / 0001 0011 0111 1111
# dp[자리수][끝자리] = dp[자리수][끝자리 - 1] + dp[자리수 - 1][끝자리]

dp = [[1 for _ in range(10)] for _ in range(n)]

for i in range(n):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[n - 1][9] % 10007)