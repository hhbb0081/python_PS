h, m = map(int, input().split())
if m >= 45:
    print(h, m - 45)
elif h > 0:
    print(h - 1, 15 + m)
else:
    print('23', 15 + m)
