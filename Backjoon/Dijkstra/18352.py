# 18352 특정 거리의 도시 찾기 (실버2)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] #  2차원 배열
distance = [INF] * (n+1)  # 거리 배열

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # (노드, 가중치) 쌍 삽입

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 우선순위 큐에 (거리, 노드) 쌍 삽입
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 거리, 노드
        if distance[now] < dist: continue  # 이미 최단 경로가 발견된 노드의 경우
        for j in graph[now]:  # 인접한 노드 순회
            cost = dist + j[1]  # 현재 거리 + 가중치
            if cost < distance[j[0]]:  # 해당 노드의 거리가 최소값인지 확인
                distance[j[0]] = cost  # 최소값이라면 갱신
                heapq.heappush(q, (cost, j[0]))  # 우선순위 큐에 삽입

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')