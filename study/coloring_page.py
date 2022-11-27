import sys
sys.stdin = open("coloring_page_input.txt")
T = int(input())

for t in range(1, T + 1):
    n = int(input())
    count = 0
    paper = [[''] * 10 for j in range(10)]
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == 1:
                    paper[r][c] += '1'
                else:
                    paper[r][c] += '2'

    for i in range(10):
        for j in range(10):
            if '1' in paper[i][j] and '2' in paper[i][j]:
                count += 1
    print(f'#{t} {count}')
