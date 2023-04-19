n = int(input())
arr = [input() for _ in range(n)]
res = ''
for i in range(len(arr[0])):
    same = ''
    for j in range(n):
        if j == 0:
            same = arr[j][i]
        else:
            if same != arr[j][i]:
                res += '?'
                break
    else:
        res += same
    
print(res)