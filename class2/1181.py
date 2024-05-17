# 1181 단어 정렬
n = int(input())
s_list = [input() for _ in range(n)]
s_list = list(set(s_list)) # 중복 제거
s_list.sort(key=lambda x: (len(x), x)) # 이중 정렬 (길이, 사전 순)
for st in s_list:
    print(st)
