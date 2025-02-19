def bsearch(diffs, times, limit, level):
    n = len(diffs)
    total = 0

    for i in range(n):
        if diffs[i] > level:
            curPrev = times[i]
            if i > 0:
                total += (curPrev + times[i - 1]) * (diffs[i] - level) + curPrev
            else:
                total += curPrev * (diffs[i] - level) + curPrev
        else:
            total += times[i]

    if total <= limit:
        return True
    else:
        return False


def solution(diffs, times, limit):
    low = 1
    high = max(diffs)

    while low <= high:
        mid = (low + high) // 2

        result = bsearch(diffs, times, limit, mid)
        if result:
            high = mid - 1
        else:
            low = mid + 1

    return low