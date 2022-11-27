import sys
sys.stdin = open("길찾기_input.txt")

for t in range(1, 11):
    tc, N = map(int, input().split())
    lst = list(map(int, input().split()))
    sol = [[] for _ in range(100)]
    visit = [0] * 100
    for i in range(0, N * 2, 2):
        sol[lst[i]].append(lst[i + 1])
    stack = [0]
    while stack:
        now = stack.pop()
        visit[now] = 1
        for j in sol[now]:
            if visit[j] == 0:
                stack.append(j)
        if visit[99]:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')

