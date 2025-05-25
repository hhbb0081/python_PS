# 1043_거짓말
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))
t = truth[0]
del truth[0]

parent = [i for i in range(n + 1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    da = find(a)
    db = find(b)
    if da != db:
        parent[db] = da

# 파티 그룹끼리 연결하기
party = [[] for _ in range(m)]
for i in range(m):
    party[i] = list(map(int, input().split()))
    del party[i][0]
    first = party[i][0]
    for j in range(1, len(party[i])):
        union(first, party[i][j])

# 진실 그룹이랑 한 명씩 비교하면서 모든 파티 확인
result = 0
for i in range(m):
    first = party[i][0]
    isConnect = False
    for j in range(len(truth)):
        if find(first) == find(truth[j]):
            isConnect = True
            break
    if not isConnect:
        result += 1

print(result)
