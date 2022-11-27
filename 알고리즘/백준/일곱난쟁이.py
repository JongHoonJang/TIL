lst = [int(input()) for _ in range(9)]

for i in range(1 << 9):
    result = []
    cnt = 0
    for j in range(9):
        if i & (1 << j):
            result.append(lst[j])
            cnt += 1
    if cnt == 7 and sum(result) == 100:
        for p in sorted(result):
            print(p)
        break

