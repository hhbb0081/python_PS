# 15681_트리와 쿼리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(n - 1)]
queries = [int(input()) for _ in range(q)]

visited = [False for _ in range(n)]
count = [0 for _ in range(n)] # 자식 노드 개수
graph = {} # 그래프

for i in range(n):
    graph[i + 1] = []

for u, v in edge:
    graph[u].append(v)
    graph[v].append(u)

# 재귀를 통해서 모든 노드의 자식 노드의 개수를 구함
def countNode(cur):
    visited[cur - 1] = True
    if len(graph[cur]) == 0:
        count[cur - 1] = 1
        return 1

    count[cur - 1] += 1
    for child in graph[cur]:
        if not visited[child - 1]:
            count[cur - 1] += countNode(child)

    return count[cur - 1]

countNode(r)
for que in queries:
    print(count[que - 1])
