import collections
def solution2(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

def solution(s):
    s = list(s[1: -1].split('{'))
    tu = []
    answer = []
    for ss in s:
        if ss != '':
            tmp = ss.rstrip().split('}')[0].split(',')
            tu.append(tmp)
    tu.sort(key=len)

    for a in tu:
        for b in a:
            b = int(b)
            if b not in answer:
                answer.append(b)
    print(answer)

    return answer

solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution2("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution2("{{20,111},{111}}")
solution2("{{123}}")
solution2("{{4,2,3},{3},{2,3,4,1},{2,3}}")