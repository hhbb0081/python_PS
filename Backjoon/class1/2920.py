n_list = list(map(int, input().split()))

if n_list == sorted(n_list):
    print('ascending')
elif n_list == sorted(n_list, reverse=True):
    print('descending')
else:
    print('mixed')