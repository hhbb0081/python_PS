# 2579 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
n_list = [0] * 301  # 초기값 설정해줘야하기 때문에 컴프리헨션 쓰면 index 에러
for i in range(n):
    n_list[i] = int(input())

dp = [0] * 301
dp[0] = n_list[0]
dp[1] = n_list[1] + dp[0]
dp[2] = max(n_list[0], n_list[1]) + n_list[2]

for i in range(3, n):
    dp[i] = max(dp[i - 3] + n_list[i - 1], dp[i - 2]) + n_list[i]
print(dp[n - 1])