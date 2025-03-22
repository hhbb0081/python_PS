import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

ss = [num[0]]

for i in range(1, n):
    ss.append(num[i] + ss[i - 1])

print(ss)

ans = 0
for x in range(n):
    for y in range(x):
        Sum = ss[x]
        if y != 0:
            Sum -= ss[y]
        print(x, y, Sum)
        if (Sum % m == 0):
            ans += 1

print(ans)