import sys
sys.stdin = open("백만장자_input.txt")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    sol = 0
    maxIdx = lst[N - 1]
    for i in range(N - 2, -1, -1):
        if maxIdx < lst[i]:
            maxIdx = lst[i]
        else:
            sol += (maxIdx - lst[i])
    # sol = 0
    # s = 0
    # maxIdx = 0
    # while s < N:
    #     maxIdx = s
    #     for i in range(s, N):
    #         if lst[maxIdx] < lst[i]:
    #             maxIdx = i
    #     for i in range(s, maxIdx):
    #         sol += lst[maxIdx] - lst[i]
    #     s = maxIdx + 1
    print(f'#{t} {sol}')
