# 1978 소수 찾기
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

t = int(input())
n_list = map(int, input().split())
cnt = 0
for n in n_list:
    if is_prime(n) == True:
        cnt += 1

print(cnt)
