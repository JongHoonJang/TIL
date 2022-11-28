import sys

sys.stdin = open("IM_01")
T = int(input())
paper = [[0 for i in range(101)] for j in range(101)]

for area in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            paper[x][y] = 1

answer = 0
for row in paper:
    answer += sum(row)
print(answer)


