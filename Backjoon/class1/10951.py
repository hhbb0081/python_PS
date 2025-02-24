# 10951 A + B - 4
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except: # 입력 없는 경우
        break