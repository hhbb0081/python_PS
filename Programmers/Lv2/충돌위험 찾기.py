def findRoutes(cur, des, pRoutes):
    cr = cur[0]
    cc = cur[1]
    dr = des[0]
    dc = des[1]

    if cr == dr and cc == dc:
        return pRoutes

    pRoutes.append(cur)

    if cr < dr:
        findRoutes([cr + 1, cc], des, pRoutes)
    elif cr > dr:
        findRoutes([cr - 1, cc], des, pRoutes)
    else:
        if cc < dc:
            findRoutes([cr, cc + 1], des, pRoutes)
        elif cc > dc:
            findRoutes([cr, cc - 1], des, pRoutes)

    return pRoutes


def solution(points, routes):
    answer = 0
    total = []

    for i in range(len(routes)):
        pRoutes = []
        for j in range(len(routes[i])):
            if j != len(routes[i]) - 1:
                cur = points[routes[i][j] - 1]
                des = points[routes[i][j + 1] - 1]
                pRoutes = findRoutes(cur, des, pRoutes)
            else:
                pRoutes.append(points[routes[i][j] - 1])
        total.append(pRoutes)
    # print(total)

    for k in range(max(len(sub_total) for sub_total in total)):
        one = []
        for m in range(len(routes)):
            if k <= len(total[m]) - 1:
                o = total[m][k]
                one.append((o[0], o[1]))
        n = len(one)
        for sub_one in list(set(one)):
            if one.count(sub_one) > 1:
                answer += 1

    return answer