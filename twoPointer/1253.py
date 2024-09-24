# 1253 좋다

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(n):
    cur = arr[i]
    s_idx = 0
    e_idx = n - 1
    while s_idx < e_idx:
        s = arr[s_idx] + arr[e_idx]
        if s == cur:
            if s_idx != i and e_idx != i:
                ans += 1
                break
            elif s_idx == i:
                s_idx += 1
            elif e_idx == i:
                e_idx -= 1
        elif s < cur:
            s_idx += 1
        else:
            e_idx -= 1





print(ans)