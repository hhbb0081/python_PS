# 9084 동전
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [[0 for _ in range(m + 1)] for _ in range(n)]

    # 첫 동전은 해당 동전의 간격만큼 1 넣어줌
    for i in range(0, m + 1, coins[0]):
        dp[0][i] = 1

    for i in range(1, n):
        cur = coins[i]
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = 1
            dp[i][j] = dp[i - 1][j]
            if j - cur >= 0:
                dp[i][j] += dp[i][j - cur]

    print(dp[n - 1][m])