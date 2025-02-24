# 1920 수 찾기
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

# 이진탐색
def f_binary(n_list, x, s, e):
    if s > e:
        return -1
    mid = (s + e) // 2
    if n_list[mid] == x:
        return mid

    elif n_list[mid] < x:
        return f_binary(n_list, x, mid + 1, e)
    else:
        return f_binary(n_list, x, s, mid - 1)

for x in m_list:
    ans = f_binary(n_list, x, 0, n - 1)
    if ans == -1:
        print(0)
    else:
        print(1)