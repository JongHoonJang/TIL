import sys
sys.stdin = open("행열찾기_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]


