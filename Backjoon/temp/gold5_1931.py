# 1931 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
sessions = [list(map(int, input().split())) for _ in range(n)]

# print(n, sessions)
sessions.sort(key=lambda x: (x[1], x[0]))

ans = 0
cur = 0
time = sessions[cur][0]
while cur < n:
    s, e = sessions[cur]
    if s >= time:
        time = e
        ans += 1
    cur += 1
print(ans)