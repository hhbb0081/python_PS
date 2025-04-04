# 14595_동방 프로젝트 (Large)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if m == 0:
    print(n)
    sys.exit(0)

behavior = [list(map(int, input().split())) for _ in range(m)]

# 그리디

behavior.sort()

ans = 0
i = 0
cur = 1

while i < m:
    x, y = behavior[i]

    if x <= cur:
        cur = max(cur, y)
    else:
        ans += (x - cur)
        cur = y
    i += 1

ans += (n - cur)
print(ans + 1)