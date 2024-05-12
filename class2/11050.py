# 11050 이항 계수1
n, k = map(int, input().split())
ans = 1

if n / 2 < k:
    k = n - k
for i in range(k):
    ans *= n
    n -= 1

div = 1
for j in range(2, k + 1):
    div *= j

if k == 0:
    print(1)
else:
    print(ans // div)