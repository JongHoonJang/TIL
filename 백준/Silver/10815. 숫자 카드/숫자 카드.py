import sys
input = sys.stdin.readline
N = input()
N_card = set(map(int, input().split()))
M = input()

for i in list(map(int, input().split())):
    if i in N_card:
        print(1, end=' ')
    else:
        print(0, end=' ')