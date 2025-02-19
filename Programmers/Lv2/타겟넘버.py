def DFS(idx, ss, target, numbers):
    answer = 0

    if idx == len(numbers):
        if ss == target:
            return 1
        else:
            return 0

    cur = numbers[idx]

    answer += DFS(idx + 1, ss + cur, target, numbers)
    answer += DFS(idx + 1, ss - cur, target, numbers)

    return answer;

def solution(numbers, target):
    nows = DFS(0, 0, target, numbers)

    return nows