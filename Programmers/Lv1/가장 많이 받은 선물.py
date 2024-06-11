# 가장 많이 받은 선물
def solution(friends, gifts):
    l = len(friends)
    scores = [0] * l # 선물 지수 리스트
    presents = [[0 for _ in range(l)] for _ in range(l)]  # 주고 받은 선물 표
    answer = 0

    for g in gifts:
        A, B = g.split()
        aidx = friends.index(A)
        bidx = friends.index(B)
        scores[aidx] += 1 # 선물 준 경우 선물 지수 + 1
        scores[bidx] -= 1 # 선물 받은 경우 선물 지수 -1
        presents[aidx][bidx] += 1 # 주고 받은 선물 갱신

    for i in range(len(friends)):
        tmp = 0
        for j in range(len(friends)):
            if i == j:
                continue
            else:
                Sub = presents[i][j] - presents[j][i]
                if Sub > 0:
                    tmp += 1
                    continue
                elif Sub == 0:
                    # 기록 없는 경우 || 주고 받은 수가 같은 경우 => 선물 지수 비교
                    if scores[i] > scores[j]:
                        tmp += 1
        answer = max(tmp, answer)

    return answer