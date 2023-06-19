n = int(input())

if n < 10:
    print(n)
else:
    cnt = 9
    for i in range(10, n + 1):
        res = 0
        for j in str(i):
            res += int(j)
        else:
            if i % res == 0:
                cnt += 1
    print(cnt)
        

