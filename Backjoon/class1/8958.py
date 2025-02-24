# 8958 OX퀴즈
t = int(input())
for _ in range(t):
    st = input()
    cnt = 0
    Sum = 0
    for s in st:
        if s == 'O':
            cnt += 1
            Sum += cnt
        else:
            cnt = 0
    print(Sum)