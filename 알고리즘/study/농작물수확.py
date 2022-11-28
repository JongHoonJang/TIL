import sys
sys.stdin = open("농작물_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    middle = N//2
    start = middle
    end = middle
    result = 0
    for i in range(N):
        for j in range(start, end+1):
            result += arr[i][j]
        if i < middle:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{tc} {result}')






