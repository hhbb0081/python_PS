# 2292 벌집
n = int(input())

if n == 1: print(1)
else:
    n -= 1
    i = 1
    while True:
        n -= (6 * i)
        if n <= 0:
            print(i + 1)
            break;
        else:
            i += 1