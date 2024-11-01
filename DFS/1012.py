# 1012 유기농 배추
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input())

# 오 위 왼 아
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]


def dfs(y, x, visited, m, n):
    visited[y][x] = True
    for i in range(4):
        next_x = x + dir_x[i]
        next_y = y + dir_y[i]
        if 0 <= next_y <= n and 0 <= next_x <= m and field[next_y][next_x] == 1 and visited[next_y][next_x] == False:
            dfs(next_y, next_x, visited, m, n)


for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    ans = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and visited[i][j] == False:
                dfs(i, j, visited, m, n)
                ans += 1
    print(ans)
