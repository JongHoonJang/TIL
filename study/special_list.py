import sys
sys.stdin = open("special_list_input.txt")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N - 1):
        minIdx = i
        maxIdx = i
        for j in range(i + 1, N):
            if a[minIdx] > a[j]:
                minIdx = j
            elif a[maxIdx] < a[j]:
                maxIdx = j
        if i % 2:
            a[i], a[minIdx] = a[minIdx], a[i]
        else:
            a[i], a[maxIdx] = a[maxIdx], a[i]
    result = ' '.join([str(i) for i in a[0:10]])
    print(f'#{t} {result}')
