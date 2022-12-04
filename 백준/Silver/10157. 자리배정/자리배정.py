c, r = map(int, input().split())
num = int(input())
lst = [[0] * r for _ in range(c)]
k = 1
i = 0
j = -1
d = 1
s = 0
if num > (r * c):
    print(0)
else:
    while r*c > 0:
        for n in range(r):
            j += d
            lst[i][j] = k
            k += 1
        else:
            r -= 1
        for m in range(c - 1):
            i += d
            lst[i][j] = k
            k += 1
        else:
            c -= 1
            d = d * -1
    else:
        for di in range(len(lst)):
            for dj in range(len(lst[di])):
                if lst[di][dj] == num:
                    print(di + 1, dj + 1)