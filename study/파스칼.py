T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    sol = []
    for i in range(N):
        sol.append([])
        sol[i].append(1)
        for j in range(1, i):
            sol[i].append(sol[i - 1][j - 1] + sol[i - 1][j])
        if i > 0:
            sol[i].append(1)
    for i in range(N):
        print(' '.join([str(n) for n in sol[i]]))





















