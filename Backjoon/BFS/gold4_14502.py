# 14502_연구소

from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)]

x_dir = [1, -1, 0, 0]
y_dir = [0, 0, 1, -1]

empty = [] # 빈공간 위치
virus = [] # 바이러스 위치
answer = 0

for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 0:
            empty.append((i, j))
        elif laboratory[i][j] == 2:
            virus.append((i, j))

def BFS():
    copy_lab = deepcopy(laboratory)
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + x_dir[i]
            ny = y + y_dir[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copy_lab[nx][ny] == 0:
                    queue.append((nx, ny))
                    copy_lab[nx][ny] = 2

    global answer
    answer = max(answer, sum(row.count(0) for row in copy_lab))


for a, b, c in combinations(empty, 3):
    # print(a, b, c)
    for x, y in [a, b, c]:
        laboratory[x][y] = 1
    BFS()
    for x, y in [a, b, c]:
        laboratory[x][y] = 0

print(answer)
