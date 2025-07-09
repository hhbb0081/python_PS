# 15650_N과 M (@)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
ans = []

def solution(cur):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(cur, n + 1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            solution(cur + 1)
            visited[i] = False
            ans.pop()

solution(1)