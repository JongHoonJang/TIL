import sys
sys.stdin = open("14696")

T = int(input())
for t in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.pop(0)
    B.pop(0)
    result = ''
    i = 4
    while i > 0:
        if A.count(i) > B.count(i):
            result = 'A'
            break
        elif A.count(i) < B.count(i):
            result = 'B'
            break
        else:
            i -= 1
    else:
        result = 'D'
    print(result)
