N = int(input())
j = 1
for i in range(1, 2 * N + 1):
    if i <= N:
        print('*' * i)
    else:
        print('*' * (N - j))
        j += 1