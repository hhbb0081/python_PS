# 1940 주몽

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()

s_idx = 0
e_idx = len(a) - 1
ans = 0

while s_idx < e_idx:
    if a[s_idx] + a[e_idx] < m:
        s_idx += 1
    elif a[s_idx] + a[e_idx] > m:
        e_idx -= 1
    else:
        ans += 1
        s_idx += 1
        e_idx -= 1

print(ans)