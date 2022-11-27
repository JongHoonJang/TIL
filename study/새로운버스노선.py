T = int(input())
for t in range(1, T + 1):
    N = int(input())
    busstop = [0] * 1001
    for n in range(N):
        bus = list(map(int, input().split()))
        if bus[0] == 1:
            for i in range(bus[1],bus[2] + 1):
                busstop[i] += 1
        elif bus[0] == 2:
            for i in range(bus[1],bus[2] + 1, 2):
                busstop[i] += 1
        elif bus[0] == 3:
            if bus[1] % 2:
                for i in range(bus[1],bus[2] + 1):
                    if i % 3 == 0 and i % 10 == 0:
                        busstop[i] += 1
            else:
                for i in range(bus[1],bus[2] + 1):
                    if i % 4 == 0:
                        busstop[i] += 1

    print(f'#{t} {max(busstop)}')