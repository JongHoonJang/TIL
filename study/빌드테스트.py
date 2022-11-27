T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                di, dj = i, j
                break
    s = 1
    while s < N:
        if 0 <= di + s < N and lst[di + s][dj] != 1:
            lst[di + s][dj] = 1
            s += 1
        else:
            break
    s1 = 1
    while s1 < N:
        if 0 <= di - s1 < N and lst[di - s1][dj] != 1:
            lst[di - s1][dj] = 1
            s1 += 1
        else:
            break
    s2 = 1
    while s2 < N:
        if 0 <= dj + s2 < N and lst[di][dj + s2] != 1:
            lst[di][dj + s2] = 1
            s2 += 1
        else:
            break
    s3 = 1
    while s3 < N:
        if 0 <= dj - s3 < N and lst[di][dj - s3] != 1:
            lst[di][dj - s3] = 1
            s3 += 1
        else:
            break
    result = 0
    for ls in lst:
        result += ls.count(0)
    print(f'#{t} {result}')



