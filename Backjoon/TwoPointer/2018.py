# 2018 (수들의 합 5)

import sys
input = sys.stdin.readline

n = int(input())

s_idx = 1
e_idx = 1
sum = 1
ans = 1

while e_idx < n:
    if sum > n:
        sum -= s_idx
        s_idx += 1
    elif sum < n:
        e_idx += 1
        sum += e_idx
    else:
        ans += 1
        e_idx += 1
        sum += e_idx

print(ans)