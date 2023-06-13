N, M = input().split()
if len(N * int(N)) > int(M):
    print((N * int(N))[:int(M)])
else:
    print(N * int(N))