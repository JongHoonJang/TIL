T = int(input())
for t in range(1, T + 1):
    N = int(input())
    i = 0
    while True:
        if i ** 3 < N:
            i += 1
        elif i**3 == N:
            print(f'#{t} {i}')
            break
        else:
            print(f'#{t} -1')
            break
