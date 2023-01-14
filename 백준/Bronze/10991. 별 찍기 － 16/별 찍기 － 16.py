N = int(input())
k = N
for i in range(N):
    print(' ' * (k - i - 1) + '* ' * (i + 1))
