import sys
sys.stdin = open("배열최소합_input.txt")


def min_lst(idx, num):
    global min_value
    if idx == N:
        if num < min_value:
            min_value = num
        return
    if num >= min_value:
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            print(lst[idx][i])
            min_lst(idx + 1, num + lst[idx][i])
            check[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    check = [0 for _ in range(N)]
    min_value = 100
    min_lst(0, 0)
    print(f'#{t} {min_value}')


