# 15654_N과 M (5)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * (n + 1)
ans = []

def solution():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            ans.append(nums[i])
            solution()
            visited[i] = False
            ans.pop()

solution()