# 1676 팩토리얼 0의 개수
n = int(input())
cnt = 0
while n > 0:
    cnt += (n // 5) # 5의 배수 개수
    n //= 5
print(cnt)