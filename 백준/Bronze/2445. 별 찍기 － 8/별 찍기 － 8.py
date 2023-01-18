N = int(input())
k = 2 * N

for i in range(1,2 * N):
    if i <= N:
        k -= 2
        print('*' * i + ' ' * k + '*' * i)
    else:
        k += 2
        print('*' * (2 * N - i) + ' ' * k + '*' * (2 * N - i))
        