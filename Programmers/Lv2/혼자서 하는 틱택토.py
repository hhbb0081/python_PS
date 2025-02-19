def isVictory(board, moves, flag):
    # 승리 조건인지 확인
    wins = [
        # 가로 승리
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # 세로 승리
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # 대각선 승리
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for win in wins:
        list = [board[x][y] for (x, y) in win]
        if [flag, flag, flag] == list:
            return True

    return False


def solution(board):
    o = []
    x = []
    for i in range(3):
        for j in range(3):
            n = board[i][j]
            if n == 'O':
                o.append([i, j])
            elif n == 'X':
                x.append([i, j])

    oLen = len(o)
    xLen = len(x)
    if oLen < xLen or oLen > xLen + 1:
        return 0

    ov = isVictory(board, o, 'O')
    xv = isVictory(board, x, 'X')
    if ov and xv:
        return 0
    if ov and oLen - xLen != 1:
        return 0
    if xv and oLen != xLen:
        return 0

    return 1