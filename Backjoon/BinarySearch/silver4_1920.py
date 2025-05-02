# 1920 원하는 정수 찾기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

def binarySearch(s, e, target):
    mid = int((s + e) / 2)
    if s > e:
        print(0)
        return
    if a[mid] == target:
        print(1)
        return

    if a[mid] > target:
        binarySearch(s, mid - 1, target)
    else:
        binarySearch(mid + 1, e, target)

for t in b:
    binarySearch(0, n - 1, t)