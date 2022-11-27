paper = [[0] * 1001 for _ in range(1001)]
N = int(input())

for i in range(1, N + 1):
    y_p, x_p, a, b = map(int, input().split())
    for y in range(y_p, y_p + a):
        paper[y][x_p:x_p + b] = [i] * b
for k in range(1, N + 1):
    result = 0
    for lst in paper:
        result += lst.count(k)
    print(result)


