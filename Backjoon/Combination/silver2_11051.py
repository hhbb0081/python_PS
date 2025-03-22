# 11051 이항계수2
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

ans = 1
diver = 1
if n // 2 < k:
    k = n - k
for i in range(k):
    ans *= (n - i)
    diver *= (i + 1)
print(ans // diver % 10007)