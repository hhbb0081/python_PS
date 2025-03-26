# 1553 도미노 찾기
import sys
input = sys.stdin.readline
domino = [list(map(int, list(input().strip()))) for _ in range(8)]

# 브루트포스?
# 1. 숫자 별 개수 맞아야 함
# 0 * 8, 1 * 8, 2 * 8, 3 * 8, 4 * 8, 5 * 8, 6 * 8

# 00 01 02 03
# 04 05 06 11
# 12 13 14 15
# 16 22 23 24

used = [[False for _ in range(7)] for _ in range(7)]
visited = [[False for _ in range(7)] for _ in range(8)]
def DFS(x, y):
    if x == 8:
        return 1
    count = 0
    nnx, nny = x, y + 1
    if nny == 7:
        nnx, nny = x + 1, 0
    if visited[x][y]:
        return DFS(nnx, nny)
    else:
        cur = domino[x][y]
        visited[x][y] = True
        for dx, dy in [(1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 7:
                nxt = domino[nx][ny]
                if not visited[nx][ny] and not used[cur][nxt]:
                    visited[nx][ny] = True
                    used[cur][nxt] = used[nxt][cur] = True

                    count += DFS(nnx, nny)

                    visited[nx][ny] = False
                    used[cur][nxt] = used[nxt][cur] = False
        visited[x][y] = False
        return count
print(DFS(0, 0))