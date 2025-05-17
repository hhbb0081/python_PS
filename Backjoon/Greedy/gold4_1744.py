# 1744_수 묶기
from queue import PriorityQueue
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n = int(input())
minus = PriorityQueue()
plus = PriorityQueue()
zero, one = 0, 0
ans = 0
for i in range(n):
    a = int(input())
    if a < 0:
        minus.put(a)
    elif a == 0:
        zero += 1
    elif a == 1:
        one += 1
    else:
        plus.put(a * -1)

while minus.qsize() > 1:
    first = minus.get()
    second = minus.get()
    ans += first * second

if not minus.empty() and zero == 0:
    ans += minus.get()

while plus.qsize() > 1:
    first = plus.get() * -1
    second = plus.get() * -1
    ans += first * second

if not plus.empty():
    ans += plus.get() * -1

ans += one
print(ans)