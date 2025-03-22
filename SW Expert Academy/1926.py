# 1926 간단한 369게임
n = int(input())
n_list = [str(x) for x in range(1, n + 1)]
for st in n_list:
    cnt = st.count('3') + st.count('6') + st.count('9')
    if cnt == 0:
        print(st, end=' ')
    else:
        print('-' * cnt, end=' ')
