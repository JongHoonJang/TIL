paper = [[0]*100 for _ in range(100)]
result = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            paper[y][x] = 1
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            result += 1
print(result)