import sys
sys.stdin = open("그래프경로_input.txt")

T = int(input())

for t in range(1, T + 1):
    v, e = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    stack = [s]
    sol = [[]for _ in range(v + 1)]
    visit = [0] * (v + 1)
    for i in range(e):
        sol[lst[i][0]].append(lst[i][1])
    print(sol)
    while stack:
        now = stack.pop()
        visit[now] = 1
        for j in sol[now]:
            if visit[j] == 0:
                stack.append(j)
            print(stack)
        if visit[g]:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')














