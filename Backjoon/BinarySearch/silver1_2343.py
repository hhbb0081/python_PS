# 2343_기타 레선
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bluelay = list(map(int, input().split()))

s = max(bluelay)
e = sum(bluelay)

while s <= e:
    mid = int((s + e) / 2)

    sum = 0 # 구간합
    cnt = 1 # 블루레이 개수
    for i in range(n):
        if sum + bluelay[i] > mid:
            cnt += 1
            sum = 0
        sum += bluelay[i]

    # print(mid, sum, cnt)

    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1

print(s)