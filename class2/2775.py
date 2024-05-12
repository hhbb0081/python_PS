# 2775 부녀회장이 될테야
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apart = [a for a in range(1, n + 1)] # 0층

    for i in range(k):
        for j in range(1, n):
            apart[j] += apart[j - 1]
    print(apart[n - 1])
