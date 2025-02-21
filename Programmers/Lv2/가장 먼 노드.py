from collections import deque

def BFS(queue, visited, graph):
    now = 0
    visited[0] = now

    while queue:
        cur = queue.popleft()
        for g in graph[cur]:
            if visited[g - 1] == -1:
                queue.append(g)
                visited[g - 1] = visited[cur - 1] + 1

    return visited

def solution(n, edge):
    answer = 0
    graph = {}
    visited = [-1 for _ in range(n)]
    queue = deque([1])

    for i in range(n):
        graph[i + 1] = []

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    ans = BFS(queue, visited, graph)

    return ans.count(max(ans))