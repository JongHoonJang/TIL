N = int(input())
k = 1
for i in range(N - 1, -1, -1):
    print(" "*i+"*"*k)
    k += 2
    