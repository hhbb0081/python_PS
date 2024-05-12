# 1546 평균
n = int(input())
n_list = list(map(int, input().split()))
Avg = (sum(n_list) / max(n_list) * 100) / n
print(Avg)