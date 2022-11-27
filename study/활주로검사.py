import sys
sys.stdin = open("활주로_input.txt")

T = int(input())
for t in range(1, T + 1):
    N, X = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    airstrip = []
    for i in range(N):
        x_lst = []
        y_lst = []
        for j in range(N):
            x_lst.append(lst[i][j])
            y_lst.append(lst[j][i])
        airstrip.extend([y_lst, x_lst])
    cnt = 0
    brk = 1
    for air in airstrip:
        j = 1
        visited = [0] * N
        while j < N:
            if air[j] == air[j - 1]:
                j += 1
            elif abs(air[j - 1] - air[j]) > 1:
                break
            elif air[j - 1] - air[j] == -1:
                if j - X >= 0 and 1 not in visited[j-X:j]:
                    visited[j - X:j] = [1] * X
                    j += 1
                else:
                    break
            elif air[j - 1] - air[j] == 1:
                if j + X <= N and 1 not in visited[j:j + X]:
                    visited[j:j + X] = [1] * X
                    j += 1
                else:
                    break
        else:
            cnt += 1
    print(f'#{t} {cnt}')
