# 10871 X보다 작은 수
n, x = map(int, input().split())
n_list = list(map(int, input().split()))

for i in n_list:
    if i < x:
        print(i, end=' ')