# 20922_겹치는 건 싫어
from collections import Counter
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_list = list(map(int, input().split()))
counter = Counter()

start, end = 0, 0
ans = 0
while end < n:
    if counter[num_list[end]] < k:
        counter[num_list[end]] += 1
        ans = max(ans, end - start + 1)
        end += 1
    else:
        counter[num_list[start]] -= 1
        start += 1
print(ans)