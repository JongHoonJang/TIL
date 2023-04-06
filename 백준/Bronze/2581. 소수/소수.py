N = int(input())
M = int(input())
res = []
for i in range(N, M + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
