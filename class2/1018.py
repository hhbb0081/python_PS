# 1018 체스판 다시 칠하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input().rstrip() for _ in range(n)]
ans = 65

def f_count(chess, i, j):
    nw = 0 # w로 시작하는 경우 잘못된 노드의 개수
    nb = 0 # b로 시작하는 경우 잘못된 노드의 개수
    for a in range(8):
        for b in range(8):
            if ((a % 2) + (b % 2)) % 2 == 0:
                # w로 시작하는 정사각형
                if chess[i + a][j + b] != 'W':
                    nw += 1
                # b로 시작하는 정사각형
                else:
                    nb += 1
            else:
                # w로 시작하는 정사각형
                if chess[i + a][j + b] == 'W':
                    nw += 1
                # b로 시작하는 정사각형
                else:
                    nb += 1
    return min(nw, nb)

for i in range(n - 7):
    for j in range(m - 7):
        tmp = f_count(chess, i, j)
        ans = min(tmp, ans)
print(ans)
