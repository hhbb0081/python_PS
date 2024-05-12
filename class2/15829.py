# 15829 Hashing
L = int(input())
st = input()

sum = 0
for i in range(0, L):
    sum += (ord(st[i]) - 96) * (31 ** i)
    sum %= 1234567891
print(sum % 1234567891)
