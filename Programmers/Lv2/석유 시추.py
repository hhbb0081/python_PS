queue = []


def bfs(land, oils, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 0
    columns = set()

    while len(queue) > 0:
        x, y = queue.pop(0)
        cnt += 1
        visited[x][y] = True

        columns.add(y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(land) and ny >= 0 and ny < len(land[0]):
                if visited[nx][ny] == False and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    for col in columns:
        oils[col] += cnt


def solution(land):
    answer = 0

    xLen = len(land)
    yLen = len(land[0])

    visited = [[False for _ in range(yLen)] for _ in range(xLen)]
    oils = [0 for _ in range(yLen)]

    for i in range(xLen):
        for j in range(yLen):
            if visited[i][j] == False and land[i][j] == 1:
                queue.append([i, j])
                bfs(land, oils, visited)
    answer = max(oils)
    return answer