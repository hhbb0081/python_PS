import math
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 1e8

n, w = map(int, input().split())
m = float(input())
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 초기화
for i in range(n):
    x, y = map(int, input().split())
    for j in range(i + 1, n):
        a, b = map(int, input().split())
        dist = math.sqrt(pow((a - x), 2) + pow((b - y), 2))
        graph[i][j] = dist
        graph[j][i] = dist

def smallNode():
    minDist = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < minDist and not visited[i]:
            minDist = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    # for i in range(n):
        # distance