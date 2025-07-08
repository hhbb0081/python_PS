# 5430_AC
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    xs = input().rstrip()

    if n == 0:
        queue = deque()
    else:
        queue = deque(xs[1:-1].split(','))

    rCnt = 0
    flag = 0

    if n == 0:
        queue = []

    for pp in p:
        if pp == 'R':
            rCnt += 1
        elif pp == 'D':
            if len(queue) > 0:
                if rCnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                flag = 1
                print('error')
                break

    if flag == 0:
        if rCnt % 2 == 1:
            queue.reverse()
        print("[%s]" % ','.join(queue))
