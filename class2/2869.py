# 2869 달팽이는 올라가고 싶다
# 시간 제한 0.5초 => 반복문 불가
a, b, v = map(int, input().split())
ans = 1 + ((v - a) // (a - b))
if (v - a) % (a - b) != 0:
    ans += 1
print(ans)