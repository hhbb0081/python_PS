# 1259 팰린드롬수
while True:
    st = input()
    if st == '0': break

    if st == st[::-1]: # 문자열 뒤집기
        print('yes')
    else:
        print('no')
