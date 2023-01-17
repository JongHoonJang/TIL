N = int(input())
k = 1
j = N - 1
for i in range(2 * N):
    if i < N:
        print(' ' * j+ '*' * k)
        if i < (N - 1):
            j -= 1
            k += 2
    else:
        k -= 2
        j += 1
        print(' ' * j+ '*' * k)