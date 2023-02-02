s, e = map(int,input().split())
arr = [0]
for i in range(1, 51):
    for j in range(i):
        arr.append(i)
print(sum(arr[s:e+1]))