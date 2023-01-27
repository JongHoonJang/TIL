N = int(input())
arr = list(map(int,input().split()))
F = int(input())
res = 0
for i in arr:
    if F == i:
        res += 1
print(res)