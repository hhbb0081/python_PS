# 16719 ZOAC
from collections import deque
import sys
input = sys.stdin.readline
str = input().strip()

num = []

def DFS(start, end):
    if start > end:
        return

    mid = start
    for i in range(start, end + 1):
        if str[i] < str[mid]:
            mid = i

    num.append(mid)

    for i in range(len(str)):
        if i in num:
            print(str[i], end='')
    print()


    DFS(mid + 1, end)
    DFS(start, mid - 1)

DFS(0, len(str) - 1)
# 가장 사전 순으로 먼저인 알파벳 먼저 출력하는데, 지금 인덱스보다 뒤쪽에 있어야함.
# 뒤쪽에 있는 인덱스를 다 출력했으면 앞쪽 꺼 출력
