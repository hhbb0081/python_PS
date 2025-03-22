# 14500_테트로미노
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tetromino = [list(map(int, input().split())) for _ in range(n)]
shape = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],

    [(0, 1), (1, 0), (1, 1)],

    [(1,0), (2,0), (2,1)],
    [(1,0), (2,0), (2,-1)],
    [(0,1), (0,2), (1,2)],
    [(0,1), (0,2), (-1,2)],
    [(1,0), (1,1), (1,2)],
    [(1,0), (1,-1), (1,-2)],
    [(0,1), (1,1), (2,1)],
    [(0,-1), (1,-1), (2,-1)],

    [(0,1), (1,1), (1,2)],
    [(0,1), (-1,1), (-1,2)],
    [(1,0), (1,1), (2,1)],
    [(1,0), (1,-1), (2,-1)],

    [(1,1), (1,0), (1,-1)],
    [(1,1), (0,1), (-1,1)],
    [(1,0), (2,0), (1,1)],
    [(1,0), (2,0), (-1,1)]
]

ans = 0

for i in range(n):
    for j in range(m):
        for s in shape:
            total = tetromino[i][j]
            for dx, dy in s:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    total += tetromino[nx][ny]
            ans = max(ans, total)
print(ans)