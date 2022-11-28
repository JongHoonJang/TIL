import sys

sys.stdin = open("homework2_input.txt")
for T in range(1, 11):
    count = int(input())
    box = list(map(int, input().split()))
    n = 0
    while n <= count:
        for i in range(100 - 1):
            if box[i + 1] <= box[i]:
                box[i], box[i + 1] = box[i + 1], box[i]
        for j in range(100 - 2):
            if box[j + 1] >= box[j]:
                box[j], box[j + 1] = box[j + 1], box[j]
        max_value = box[-1]
        min_value = box[-2]
        box[-1] -= 1
        box[-2] += 1
        n += 1
    print(f'#{T} {max_value - min_value}')
