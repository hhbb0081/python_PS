# 14888_연산자 끼워넣기
import sys
import math
from itertools import permutations
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
op_num = list(map(int, input().split()))

# 브루트포스, 조합

op = []
for i in range(4):
    for _ in range(op_num[i]):
        op.append(i + 1)

Min, Max = 1e9, -1e9
for com in permutations(op, n - 1):
    total = nums[0]
    for c in range(1, n):
        if com[c - 1] == 1:
            total += nums[c]
        elif com[c - 1] == 2:
            total -= nums[c]
        elif com[c - 1] == 3:
            total *= nums[c]
        elif com[c - 1] == 4:
            total = int(total / nums[c])
    if total < Min:
        Min = total
    if total > Max:
        Max = total
print(Max)
print(Min)