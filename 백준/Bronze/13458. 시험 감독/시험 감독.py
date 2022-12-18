N = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
res = 0
for i in arr:
    if i - a < 0:
        res += 1
    else:
        res += 1
        if (i - a) % b == 0:
            res += ((i - a) // b)
        else:
            res += ((i - a) // b)
            res += 1
print(res)