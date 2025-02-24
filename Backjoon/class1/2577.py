mul = 1;
for _ in range(3):
    mul *= int(input()) # 수 곱하기

for num in range(0, 10):
    print(list(str(mul)).count(str(num))) # 수를 list로 바꿔 0 ~ 9까지 개수 세기