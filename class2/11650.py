# 11650 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
n_list.sort(key=lambda x: (x[0], x[1]))
for m in n_list:
    print(m[0], m[1])