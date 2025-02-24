# 7568 덩치
import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * n
k = [] # (몸무게, 키) 쌍 배열
for i in range(n):
    x, y = map(int, input().split())
    k.append((x, y))

for i in k:
    rank = 1
    for j in k:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")


