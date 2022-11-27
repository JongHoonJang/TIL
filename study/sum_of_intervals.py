import sys

sys.stdin = open("구간합_input.txt")
T = int(input())

for t in range(1, T + 1):
    count, n = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = []
    value = 0
    for i in range(count - (n - 1)):
        value = 0
        for j in range(n):
            value += numbers[i + j]
        result.append(value)
    for x in range(len(result) - 1, 0, -1):
        for y in range(x):
            if result[y] > result[y + 1]:
                result[y], result[y + 1] = result[y + 1], result[y]
    print(f'#{t} {result[len(result) - 1] - result[0]}')
