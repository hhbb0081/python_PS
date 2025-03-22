import sys
input = sys.stdin.readline

k = int(input())

# 4 7 44 47 74 77 444 447
# dp[1] = 2
# dp[2] = 2^2
# dp[3] = 2^3
# 2, 6, 14, 30
# 3 -> 2 + 1
# 10 -> 6 + 4
# 14 -> 6 + 8

ans = ''
while k > 0:
    if k % 2 == 0:
        ans += '7'
        k -= 1
    else:
        ans += '4'
    k = k // 2
print(ans)