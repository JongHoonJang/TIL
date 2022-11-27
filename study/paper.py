import sys
sys.stdin = open("paper_input.txt")


def count(c):
    if c == 20:
        return 3
    elif c == 10:
        return 1
    else:
        return count(c - 10) + 2 * count(c - 20)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    # print(f'#{t} {count(N)}')
    n = N // 10
    paper = [1, 3]
    for i in range(2, n):
        paper.append((paper[i - 1] + 2 * paper[i - 2]))

    print(f'#{t} {paper[-1]}')





