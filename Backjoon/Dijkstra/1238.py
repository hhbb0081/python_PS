# 1238 파티 (골드3)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append(e, t)

def dijkstra(s):
    q = []
    distance = [INF] * (n + 1)

    distance[s] = 0
    heapq.heapqpush(q, (0, s))
    while q:
        dist, now = heapq.heapqpop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return distance

result = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])