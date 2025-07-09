# 15655_N과 M (6)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * (n + 1)
ans = []

def solution(cur):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(cur, n):
        if not visited[i]:
            visited[i] = True
            ans.append(nums[i])
            solution(i + 1)
            visited[i] = False
            ans.pop()

solution(0)