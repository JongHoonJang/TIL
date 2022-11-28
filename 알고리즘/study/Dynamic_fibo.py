def fibo(n):
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]

    return F[n]


N = int(input())
F = [0]*(N+1)
fibo(N)
for j in range(1, N+1):
    print(F[j])
