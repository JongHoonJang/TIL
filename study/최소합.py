import sys
sys.stdin = open("최소합_input.txt")


def over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return True
    return False


def DFS(y, x):
    global value, num
    if value < num:
        return
    if y == (N - 1) and x == (N - 1):
        if value > num:
            value = num
        return
    for dy, dx in ((1, 0), (0, 1)):
        new_y, new_x = y + dy, x + dx
        if over(new_x, new_y) and not visited[new_y][new_x]:
            # visited[new_y][new_x] = 1
            num += arr[new_y][new_x]
            DFS(new_y, new_x)
            # visited[new_y][new_x] = 0
            num -= arr[new_y][new_x]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    value = 999999999
    num = arr[0][0]
    DFS(0, 0)

    print(f'#{t} {value}')
