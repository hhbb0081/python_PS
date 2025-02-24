# 단어 공부
str = input().lower() # 소문자로 바꾸기
str_list = list(set(str)) # 한 글자 씩 set에 삽입하고 list로 변경
cnt = [] # 알파벳 개수 리스트
ans = ''

for i in str_list:
    tmp = str.count(i) # 알파벳 개수 세기
    cnt.append(tmp) # 개수 리스트에 담기

if cnt.count(max(cnt)) >= 2: # 가장 많은 알파벳 개수
    print("?")
else:
    print(str_list[cnt.index(max(cnt))].upper()) # 가장 많은 알파벳의 인덱스를 이용하여 해당하는 알파벳 구하기