arr = []
for _ in range(5):
    arr.append(input())

res = ''  
for i in range(15):
    for j in range(5):
        if len(arr[j]) <= i:
            continue
        else:
            res += arr[j][i]
print(res)