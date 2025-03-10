# 14400_편의점 2
import sys
input = sys.stdin.readline

n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]

mid = n // 2
positions.sort()
mid_x = positions[mid][0]
positions.sort(key=lambda x: x[1])
mid_y = positions[mid][1]

ans = 0
for x, y in positions:
    ans += (abs(x - mid_x) + abs(y - mid_y))
print(ans)

# 맨해튼 거리