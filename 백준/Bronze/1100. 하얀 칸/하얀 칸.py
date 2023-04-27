lst = [[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1]]
arr = [input() for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if arr[i][j] == 'F':
            if i % 2:
                if lst[1][j]:
                    cnt += 1
            else:
                if lst[0][j]:
                    cnt += 1
print(cnt)