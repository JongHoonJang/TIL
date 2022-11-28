T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    value = []
    for i in range(1 << N):
        result = 0
        for j in range(N):
            if i & (1 << j):
                result += lst[j]
        if result not in value:
            value.append(result)
    print(value)
    print(f'#{t} {len(value)}')
