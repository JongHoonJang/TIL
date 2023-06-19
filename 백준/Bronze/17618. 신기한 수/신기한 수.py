import sys
n = int(sys.stdin.readline())

if n < 10:
    print(n)
else:
    cnt = 9
    for i in range(10, n + 1):
        res = sum([int(c) for c in str(i)])
        if i % res == 0:
            cnt += 1
    print(cnt)