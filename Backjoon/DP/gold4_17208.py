# 17208_카우버거 알바생
# 3차원 dp
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-1 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

def rec(che, pot, i):
    if i >= n:
        return 0

    # 이미 계산 된 값이라면
    if dp[i][che][pot] != -1:
        return dp[i][che][pot]

    dp[i][che][pot] = rec(che, pot, i + 1)
    if che >= orders[i][0] and pot >= orders[i][1]:
        dp[i][che][pot] = max(rec(che - orders[i][0], pot - orders[i][1], i + 1) + 1, dp[i][che][pot])

    return dp[i][che][pot]

print(rec(m, k, 0))