# 11724 연결 요소의 개수

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
ans = 0


def DFS(v):
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            DFS(g)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        ans += 1
print(ans)
