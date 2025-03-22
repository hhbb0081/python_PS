# 21941 문자열 제거
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

str = input()
m = int(input())
erase = [list(input().split()) for _ in range(m)]
score = [-1 for _ in range(len(str))]

def DFS(start, score):
    if start == len(str):
        return 0
    if score[start] != -1:
        return score[start]

    score[start] = DFS(start + 1, score) + 1
    for e, s in erase:
        if str[start : start + len(e)] == e:
            score[start] = max(score[start], DFS(start + len(e), score) + int(s))
    return score[start]

print(DFS(0, score) - 1)
