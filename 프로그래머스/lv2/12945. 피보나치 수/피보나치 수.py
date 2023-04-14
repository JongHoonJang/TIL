def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    fib_mem = [0] * (n + 1)
    fib_mem[0], fib_mem[1] = 0, 1
    for i in range(n - 1):
        fib_mem[i + 2] = fib_mem[i] + fib_mem[i + 1]
    
    return fib_mem[n]

def solution(n):
    return fibonacci(n) % 1234567