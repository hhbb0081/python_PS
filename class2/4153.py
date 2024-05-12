# 4153 직각삼각형
while True:
    n_list = list(map(int, input().split()))
    if n_list[0] == 0 and n_list[1] == 0 and n_list[2] == 0:
        break
    n_list = sorted(n_list)
    if n_list[0] * n_list[0] + n_list[1] * n_list[1] == n_list[2] * n_list[2]:
        print("right")
    else:
        print("wrong")
