res = 0
arr = ['N', 'E', 'S' ,'W']
for i in range(10):
    a = int(input())
    if a == 1:
        res += 1
        if res == 4:
            res = 0
    elif a == 2:
        res += 2
        if res > 3:
            res -= 4
    elif a == 3:
        res -= 1
        if res == -1:
            res = 3
print(arr[res])