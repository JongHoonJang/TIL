N = int(input())
lst = [0, 1, 2] + [0] * 999
if N >= 3:
    for i in range(3, N + 1):
        lst[i] = lst[i-2] + lst[i-1]
print(lst[N] % 10007)
