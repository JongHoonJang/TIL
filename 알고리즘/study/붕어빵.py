T = int(input())

for t in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    parson = list(map(int, input().split()))
    bread = 0
    cnt = 0
    result = 'Possible'
    for i in range(11112):
        if i % M == 0 and i > 0:
            bread += K
        if i in parson:
            bread -= parson.count(i)
            cnt += parson.count(i)
            if bread < 0:
                result = 'Impossible'
                break
            if cnt == len(parson):
                break

    print(f'#{t} {result}')
