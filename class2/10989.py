# 10989 수 정렬하기3
import sys
input = sys.stdin.readline

n = int(input())
n_list = [0] * 10001

# 계수 정렬 이용
for _ in range(n):
    n_list[int(input())] += 1

i = 0
while n > 0:
    if n_list[i] > 1:
        print(i)
        n_list[i] -= 1
        n -= 1
    elif n_list[i] == 1:
        print(i)
        n_list[i] -= 1
        i += 1
        n -= 1
    else:
        i += 1
