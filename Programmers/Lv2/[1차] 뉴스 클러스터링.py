def solution(str1, str2):
    answer = 0
    # 대소문자 구분 없애기
    ss1 = list(str1[i: i + 2].lower() for i in range(len(str1) - 1) if str1[i: i + 2].isalpha()) # str1 두 글자씩 끊기
    ss2 = list(str2[i: i + 2].lower() for i in range(len(str2) - 1) if str2[i: i + 2].isalpha()) # str2 두 글자씩 끊기

    css1 = Counter(ss1)
    css2 = Counter(ss2)

    iLen = len(list((css1 & css2).elements())) # counter 교집합 길이
    uLen = len(list((css1 | css2).elements())) # counter 합집합 길이

    if iLen == 0 and uLen == 0:
        answer = 65536
    else:
        answer = int(iLen / uLen * 65536)
    # print(answer)
    return answer

import re
from collections import Counter

solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")