def fibo(n):
    if n <= 2:
        return 1
    if m[n] != '':
        return m[n]

    m[n] = fibo(n-1) + fibo(n-2)

    return m[n]


N = int(input())
m = ['']*(N+1)
fibo(N)
print(m[N])
print(fibo(N))


