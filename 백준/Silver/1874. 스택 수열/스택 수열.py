n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
i = 1
res = []
while arr != []:
    if i > n + 1:
        break
    if stack == [] or stack[-1] != arr[0]:
        stack.append(i)
        res.append('+')
        i += 1
    elif stack[-1] == arr[0]:
        stack.pop()
        arr.pop(0)
        res.append('-')
    
if arr:
    print('NO')
else:
    for r in res:
        print(r)
    
        