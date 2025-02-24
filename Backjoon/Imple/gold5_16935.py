# 16935_배열 돌리기3
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
a_list = list(map(int, input().split()))

for _ in range(max(n, m) - min(n, m)):
    arr.append([0] * m)

# 1번 (상하 반전)
# arr[n - i - 1][j]
# 위쪽 절반만

# 2번 (좌우 반전)
# arr [i][m - j - 1]
# 왼쪽 절반만

# 3번 (오른쪽 90도 회전)
# (0, 0) <-> (n - 1, 0) <-> (n - 1, m - 1) <-> (n - 1, 0)
# (0, 1) <-> (n - 2, 0) <-> (n - 1, m - 2)
# m - (n - (n - 2)) = m - n +
# arr[j][m - i - 1]
# 1 -> 4 -> 3 -> 2 (반시계 방향으로)

# 4번 (왼쪽 90도 회전)
# arr[n - j - 1][i]
# 1 -> 2 -> 3 -> 4 (시계 방향으로)

# 5번 (시계 90도 회전)
# 1번: (i, j) -> (i, j + m / 2) []
# 2번: (i, j) -> (i + n / 2, j) [j + 2 / m > m]
# 3번: (i, j) -> (i, j - n / 2) [i + 2 / n > n && j + 2 / m > m]
# 4번: (i, j) -> (i - n / 2, j) [i + 2 / n > n]
# 4 -> 3 -> 2 -> 1 순으로 swap

# 6번
# 1번: (i, j) -> (i + n / 2, j + m / 2)
# 2번: (i, j) -> (i, j - m / 2)
# 3번: (i, j) -> (i - n / 2, j + m / 2)
# 4번: (i, j) -> (i, j - m / 2)
# 1 -> 2 -> 3 -> 4 순으로 swap

# 순환돼야한

for a in range(len(a_list)):
    new_arr = []
    # 1번 (상하 반전)
    if a_list[a] == 1:
        for i in range(n):
            new_col = []
            for j in range(m):
                new_col.append(arr[n - i - 1][j])
            new_arr.append(new_col)

    # 2번 (좌우 반전)
    elif a_list[a] == 2:
        for i in range(n):
            new_col = []
            for j in range(m):
                new_col.append(arr[i][m - j - 1])
            new_arr.append(new_col)

    # 3번 (오른쪽 90도 회전)
    elif a_list[a] == 3:
        for i in range(m):
            new_col = []
            for j in range(n):
                new_col.append(arr[n - j - 1][i])
            new_arr.append(new_col)
        n, m = m, n

    # 4번 (왼쪽 90도 회전)
    elif a_list[a] == 4:
        for i in range(m):
            new_col = []
            for j in range(n):
                new_col.append(arr[j][m - i - 1])
            new_arr.append(new_col)
        n, m = m, n

    # 5번 (사분면 시계 방향 회전)
    elif a_list[a] == 5:
        for i in range(n):
            new_col = []
            for j in range(m):
                if i < n // 2:
                    if j < m // 2:
                        # 1 사분면
                        new_col.append(arr[i + n // 2][j])
                    else:
                        # 2 사분면
                        new_col.append(arr[i][j - m // 2])
                else:
                    if j >= m // 2:
                        # 3 사분면
                        new_col.append(arr[i - n // 2][j])
                    else:
                        # 4 사분면
                        new_col.append(arr[i][j + m // 2])
            new_arr.append(new_col)

    # 6번 (사분면 반시계 방향 회전)
    else:
        for i in range(n):
            new_col = []
            for j in range(m):
                if i < n // 2:
                    if j < m // 2:
                        # 1 사분면
                        new_col.append(arr[i][j + m // 2])
                    else:
                        # 2 사분면
                        new_col.append(arr[i + n // 2][j])
                else:
                    if j >= m // 2:
                        # 3 사분면
                        new_col.append(arr[i][j - m // 2])
                    else:
                        # 4 사분면
                        new_col.append(arr[i - n // 2][j])
            new_arr.append(new_col)

    arr = new_arr

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()