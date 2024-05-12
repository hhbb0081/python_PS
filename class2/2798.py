# 2798 블랙잭
n, m = map(int, input().split())
c_list = list(map(int, input().split()))
c_list.sort()

Max = 0
for i in range(0, len(c_list)):
    sum = c_list[i]
    for j in range(i + 1, len(c_list)):
        sum += c_list[j]
        for k in range(j + 1, len(c_list)):
            sum += c_list[k]
            if sum <= m and sum > Max:
                Max = sum
            sum -= c_list[k]
        sum -= c_list[j]
    sum -= c_list[i]

print(Max)
# 시간 복잡도 : 100 * 100 * 100 == 1,000,000ms