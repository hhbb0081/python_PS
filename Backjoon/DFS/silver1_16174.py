# 16174 점프왕 쩰리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def solution(x, y):
    if x == y == n - 1:
        visited[x][y] = True
        return

    cur = game[x][y]
    for nx, ny in [(x + cur, y), (x, y + cur)]:
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            solution(nx, ny)
    return

solution(0, 0)
if visited[n - 1][n - 1]:
    print("HaruHaru")
else:
    print("Hing")