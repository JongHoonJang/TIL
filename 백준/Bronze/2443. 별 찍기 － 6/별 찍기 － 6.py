N = int(input())
j = 0
k = N
for i in range(N):
    print(' ' * j + "*" * (2 * k - 1))
    j += 1
    k -= 1
