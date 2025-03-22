# 16938_캠프 준비
import sys
from collections import deque
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
level = list(map(int, input().split()))
level.sort()
visited = [False for _ in range(n)]
global ans
ans = 0

# # 2 ~ n 개의 조합 구해서 순회하면서 조건 맞는지 확인
# for i in range(2, n + 1):
#     combination = list(combinations(level, i))
#     for com in combination:
#         com = sorted(com)
#         if com[-1] - com[0] >= x and l <= sum(com) <= r:
#             ans += 1

queue = []
def DFS(start, cnt):
    global ans
    if cnt == n:
        return

    for i in range(start, n):
        if visited[i] == True:
            continue
        visited[i] = True
        queue.append(level[i])

        if l <= sum(queue) <= r and queue[len(queue) - 1] - queue[0] >= x:
            ans += 1

        DFS(i + 1, cnt + 1)

        visited[i] = False
        queue.pop()

DFS(0, 0)
print(ans)