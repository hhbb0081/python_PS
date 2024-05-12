# 2609 최대공약수와 최소공배수

# 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수
def lcm(a, b, m):
    Min = a * b // m
    return Min

a, b = map(int, input().split())
m = gcd(a, b)
print(m)
print(lcm(a, b, m))