import sys
sys.stdin = open("주사위")

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
result = 0
i = 0


