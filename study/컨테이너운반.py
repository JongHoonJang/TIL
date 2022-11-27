import sys
sys.stdin = open("컨테이너_input.txt")


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort()
    truck.sort()
    move = 0
    i = len(container) - 1
    j = len(truck) - 1
    while i >= 0 and j >= 0:
        if container[i] <= truck[j]:
            move += container[i]
            j -= 1
        i -= 1
    print(f'#{t} {move}')
