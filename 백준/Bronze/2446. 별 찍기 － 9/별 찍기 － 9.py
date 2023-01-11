N = int(input())
j = 0
k = N
for i in range(2 * N - 1):
    if i >= N:
        j -= 1
        k += 1
        print(' ' * j + "*" * (2 * k - 1))
    else:
        print(' ' * j + "*" * (2 * k - 1))
        j += 1
        if k > 1:
            k -= 1
        else:
            j -= 1


