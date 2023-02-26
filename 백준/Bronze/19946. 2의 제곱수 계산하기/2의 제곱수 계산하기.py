N = int(input())
k = 64
while N % 2 == 0:
    N //= 2
    k -= 1
print(k)