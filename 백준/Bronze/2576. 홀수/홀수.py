res = []
for i in range(7):
    N = int(input())
    if N % 2 == 1:
        res.append(N)
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))