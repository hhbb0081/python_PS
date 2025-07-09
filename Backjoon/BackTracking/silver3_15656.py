# 15656_N과 M (7)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def solution():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(n):
        ans.append(nums[i])
        solution()
        ans.pop()

solution()