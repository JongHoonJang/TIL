N = int(input())
arr = [input() for _ in range(N)]
i = 1
res = []
while len(res) != len(set(arr)):
    cnt = []
    for a in set(arr):
        if len(a) == i and a not in cnt:
            cnt.append(a)
    else:
        cnt.sort()
        res.extend(cnt)
        i += 1
for r in res:
    print(r)