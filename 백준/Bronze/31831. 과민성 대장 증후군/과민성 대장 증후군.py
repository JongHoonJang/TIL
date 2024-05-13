day, max_s = map(int, input().split())
s_lst = list(map(int, input().split()))
cnt = 0
s = 0
for i in s_lst:
    s += i
    if s >= max_s:
        cnt += 1
    if s < 0:
        s = 0
print(cnt)