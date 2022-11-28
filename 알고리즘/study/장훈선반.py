import sys
sys.stdin = open("장훈선반input.txt")

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    value = 99999999
    for i in range(1 << N):
        result = 0
        for j in range(N):
            if i & (1 << j):
                result += lst[j]
        if result >= B:
            if value > result:
                value = result
    print(f'#{t} {value - B}')
