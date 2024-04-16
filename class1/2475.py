num_list = list(map(int, input().split()))
ans = 0;
for i in num_list:
    ans += (i * i) % 10
print(ans % 10)