# 1976_여행 가자
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
city = [list(map(int, input().split())) for _ in range(n)]
route = list(map(int, input().split()))

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            union(i + 1, j + 1)

index = find(route[0])

for i in range(1, n):
    if find(route[i]) != index:
        print('NO')
        exit(0)

print('YES')

