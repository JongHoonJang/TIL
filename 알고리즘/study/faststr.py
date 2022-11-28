import sys
sys.stdin = open("faststr_input.txt")
T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    A_lange = len(A)
    B_lange = len(B)
    result = len(A)
    i = 0
    # print(f'#{tc} {A_lange - ((B_lange - 1) * A.count(B))}')
    while i < A_lange:
        if A[i] == B[0]:
            if A[i:i + B_lange] == B:
                result -= (B_lange - 1)
                i += B_lange
            else:
                i += 1
        else:
            i += 1
    print(f'#{tc} {result}')
