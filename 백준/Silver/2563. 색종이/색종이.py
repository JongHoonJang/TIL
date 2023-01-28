N = int(input())
arr = [([0] * 101) for _ in range(101)]
res = 0
for i in range(N):
    x, y = map(int, input().split())
    for i in range(1, 11):
        for j in range(1, 11):
            if arr[x + j][y + i] ==0:
                arr[x + j][y + i] = 1
for r in arr:
    res += sum(r)
print(res)