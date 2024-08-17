import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[0] * (n + 1)]
s = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    ll = [0] + list(map(int, input().split()))
    table.append(ll)

# 합 배열 구하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
    print(result)
