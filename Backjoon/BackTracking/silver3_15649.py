# 15649_N과 M(1)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
ans = []

def solution():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for cur in range(1, n + 1):
        if not visited[cur]:
            visited[cur] = True
            ans.append(cur)
            solution()
            ans.pop()
            visited[cur] = False

solution()