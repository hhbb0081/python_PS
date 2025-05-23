# 1541_잃어버린 괄호
import sys
input = sys.stdin.readline

exp = input().strip()

# 55-(50+40) => 마이너스 다음에 있는 숫자 괄호 치기, 플러스 나올 때까지
# 55-50-40
# 55-50+40-10+100

mlist = exp.split('-')
ans = 0

for i in range(len(mlist)):
    sum = 0
    mmlist = mlist[i].split('+')
    for mm in mmlist:
        sum += int(mm)

    if i == 0:
        ans += sum
    else:
        ans -= sum
print(ans)
