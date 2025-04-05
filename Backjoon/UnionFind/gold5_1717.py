# 1717_집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
num_list = [i for i in range(n + 1)]

def find(idx):
    if idx == num_list[idx]:
        return idx
    # 부모 노드가 존재하는 경우 부모 노드 값으로 갱신
    else:
        num_list[idx] = find(num_list[idx])
        return num_list[idx]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        num_list[pb] = pa

for _ in range(m):
    t, a, b = map(int, input().split())
    # 합집합 연산
    if t == 0:
        union(a, b)
    else:
        pa = find(a)
        pb = find(b)
        if pa == pb:
            print('YES')
        else:
            print('NO')
    # print(num_list)
