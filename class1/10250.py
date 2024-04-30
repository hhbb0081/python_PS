# 10250 ACM 호텔
t = int(input())
for _ in range(t):
    h, w, c = map(int, input().split())
    y = c % h
    x = (c // h) + 1
    if y == 0:
        y = h
        x -= 1
    print(y * 100 + x)