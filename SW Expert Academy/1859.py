# 1859 백만 장자 프로젝트
t = int(input())
for tt in range(1, t + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    m = 0
    sum = 0
    for i in n_list[::-1]:
        if i >= m:
            m = i
        else:
            sum += m - i
    print('#' + str(tt), str(sum))