# 20159_동작 그만
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
odd = [cards[0]] # 홀수
eve = [cards[1]] # 짝수

for i in range(2, len(cards)):
    idx = i // 2
    if i % 2 != 0:
        eve.append(eve[idx - 1] + cards[i])
    else:
        odd.append(odd[idx - 1] + cards[i])

ans = odd[-1]
for i in range(len(cards)):
    # i 번째 인덱스 밑장 빼기
    sum = 0
    if i % 2 == 0:
        # 내꺼 밑장 빼기
        # 만약에 2번째 인덱스 밑장 빼기면 홀수 i // 2 - 1까지만 더하기
        # 그리고 짝수 i // 2부터 끝까지
        if i // 2 == 0:
            sum = eve[-1]
            ans = max(sum, ans)
            # print(i, eve[len(eve) - 1], sum)
            continue
        sum += odd[(i // 2) - 1]
        sum += eve[-1] - eve[(i // 2) - 1]
        ans = max(sum, ans)
        # print(i, odd[(i // 2) - 1], eve[len(eve) - 1] - eve[(i // 2) - 1], sum)
    else:
        # 남의 꺼 밑장 빼기
        # 만약에 3번 째 인덱스 밑장 빼기면 홀수 i // 2 - 1까지만 더하기
        # 그리고 짝수 i // 2 - 1부터 len - 2까지
        if len(eve) < 2:
            continue

        if i // 2 == 0:
            sum += odd[i // 2]
            sum += eve[-2]
            ans = max(sum, ans)
            # print(i, odd[i // 2], eve[len(eve) - 2], sum)
            continue
        sum += odd[i // 2]
        sum += eve[-2] - eve[(i // 2) - 1]
        ans = max(sum, ans)
        # print(i, odd[i // 2], eve[len(eve) - 2] - eve[(i // 2) - 1], sum)
print(ans)