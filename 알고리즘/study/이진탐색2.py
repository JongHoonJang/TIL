import sys
sys.stdin = open("이진탐색2_input.txt")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for b in B:
        start = 0
        end = N - 1
        k = 0
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == b:
                cnt += 1
                break
            elif A[mid] > b:
                if k == 1:
                    break
                else:
                    k = 1
                    end = mid - 1
            else:
                if k == 2:
                    break
                else:
                    k = 2
                    start = mid + 1
    print(f'#{t} {cnt}')




