# 2042_구간 합 구하기
import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 트리 높이 구하기
h = 1
nn = n
while nn != 0:
    h += 1
    nn //= 2

treeSize = int(math.pow(2, h + 1))
lidx = treeSize // 2 - 1 # 트리 사이즈의 절반
tree = [0] * (treeSize + 1)

# 트리 초기화
for i in range(lidx + 1, lidx + n + 1):
    tree[i] = int(input())

# 트리 생성
j = treeSize - 1
while j != 1:
    tree[j // 2] += tree[j]
    j -= 1

# 수 업데이트
def changeVal(idx, val):
    diff = val - tree[idx]
    while idx > 0:
        tree[idx] += diff
        idx //= 2

# 구간합 구하기
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

for _ in range(m + k):
    a, b, c = map(int, input().split())
    # a가 1이면, b번째 수를 c로 바꿈
    # a가 2이면, b번째부터 c번째까지의 구간합
    if a == 1:
        changeVal(lidx + b, c)
    elif a == 2:
        b += lidx
        c += lidx
        print(getSum(b, c))

