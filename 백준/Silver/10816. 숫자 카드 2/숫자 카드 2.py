N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
find_num = list(map(int, input().split()))
res = {}
for i in cards:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

for i in find_num:
    if i in res:
        print(res[i], end=' ')
    else:
        print(0, end=' ')