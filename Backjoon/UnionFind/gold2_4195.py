# 4195_친구 네트워크
import sys
input = sys.stdin.readline

t = int(input())

def find(p):
    if p == parent[p]:
        return p
    parent[p] = find(parent[p])
    return parent[p]

def union(a, b):
    p = find(a)
    q = find(b)
    if p != q:
        parent[q] = p
        size[p] += size[q]
    print(size[p])

for _ in range(t):
    n = int(input())
    friendMap = {}
    parent = []
    size = []
    for _ in range(n):
        a, b = input().strip().split(" ")

        if a not in friendMap:
            friendMap[a] = len(parent)
            parent.append(len(parent))
            size.append(1)

        if b not in friendMap:
            friendMap[b] = len(parent)
            parent.append(len(parent))
            size.append(1)

        x = friendMap[a]
        y = friendMap[b]

        union(x, y)

