import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
if sum(arr) % 2 == 0:
    print(sum(arr))
else:
    for i in arr:
        if i % 2 == 1:
            print(sum(arr) - i)
            break
    else:
        print(0)