import sys
sys.stdin = open("병합정렬_input.txt")


def quicksort(A, left, right):
    if left >= right:
        return
    p = A[left]
    i = left
    j = right
    while i <= j:
        while i < right and A[i] <= p:
            i += 1
        while left < j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            A[left], A[j] = A[j], A[left]
    quicksort(A, left, j)
    quicksort(A, j + 1, right)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quicksort(lst, 0, N - 1)
    print(f'#{t} {lst[N // 2]}')
