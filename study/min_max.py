import sys

sys.stdin = open("min_max_input.txt")
T = int(input())

for t in range(1, T + 1):
    count = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    for i in range(count - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    result = numbers[count - 1] - numbers[0]
    print(f'#{t} {result}')
