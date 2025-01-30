def calTime(start, end):
    sh, sm = start.split(":")
    eh, em = end.split(":")
    return 60 * (int(eh) - int(sh)) + (int(em) - int(sm))


def solution(plans):
    answer = []
    stops = []
    plans.sort(key=lambda k: (k[1]))

    while len(plans) > 0:
        name, start, playtime = plans.pop(0)
        time = int(playtime)

        if plans:
            diff = calTime(start, plans[0][1])
        else:
            # 마지막 과제인 경우
            diff = time

        if time > diff:
            # 현재 과제를 끝낼 수 없는 경우 -> 남은 시간 갱신 후 대기열에 추가
            stops.append([name, start, time - diff])
        else:
            # 현재 과제를 끝낼 수 있는 경우
            answer.append(name)
            remain = diff - time

            while remain > 0 and len(stops) > 0:
                sname, sstart, stime = stops.pop()
                if remain >= stime:
                    # 남은 시간 동안 중단된 과제를 진행할 수 있는 경우
                    answer.append(sname)
                    remain -= stime
                else:
                    # 할 수 없는 경우
                    stops.append([sname, sstart, stime - remain])
                    remain -= stime

    while stops:
        answer.append(stops.pop()[0])

    return answer