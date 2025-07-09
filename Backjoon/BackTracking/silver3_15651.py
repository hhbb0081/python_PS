# 15651_N과 M (3)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

def solution():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n + 1):
        ans.append(i)
        solution()
        ans.pop()

solution()
