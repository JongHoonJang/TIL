import sys

sys.stdin = open("subset_input.txt")

T = int(input())
A = [i for i in range(1, 13)]
for t in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0
    # 부분집합 생성
    for i in range(1 << len(A)):
        value = cnt = 0 #부분집합의 합과 부분집합의 개수 초기화
        for j in range(len(A)):
            if i & (1 << j):
                value += A[j]
                cnt += 1
        #부분집합의 합이 K이고 부분집합의 개수가 N일경우
        if value == K and cnt == N:
            count += 1
    print(f'#{t} {count}')
