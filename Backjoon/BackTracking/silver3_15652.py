# 15652_N과 M (4)
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
        ans.append(i)
        solution(i)
        ans.pop()

solution(1)
