import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    garden = [input().split()[0] for _ in range(h)]

    visited = [[False for _ in range(w)] for _ in range(h)]
    x_dir = [1, -1, 0, 0]
    y_dir = [0, 0, 1, -1]

    def DFS(x, y):
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + x_dir[i], y + y_dir[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and garden[nx][ny] == '#':
                DFS(nx, ny)
        return

    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and garden[i][j] == '#':
                DFS(i, j)
                ans += 1

    print(ans)