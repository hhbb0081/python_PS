# 15558 점프 게임
from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
map = [input().strip() for _ in range(2)]


# BFS
queue = deque([(0, 0, 0)])
visited = [[False for _ in range(n)] for _ in range(2)]

while queue:
    row, idx, time = queue.popleft()


    print(row, idx, time)

    routes = [[row, idx + 1], [row, idx - 1], [1 - row, idx + k]]
    for i in range(len(routes)):
        nextRow, nextIdx = routes[i]
        if nextIdx >= n:
            print(1)
            exit()
        if time < nextIdx and not visited[nextRow][nextIdx] and map[nextRow][nextIdx] == '1':
            visited[nextRow][nextIdx] = True
            queue.append([nextRow, nextIdx, time + 1])

print(0)
