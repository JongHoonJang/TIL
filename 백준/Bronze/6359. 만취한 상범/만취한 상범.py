t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] * (n + 1) 
    for i in range(2, n + 1):
        for j in range(i,n + 1):
            if j % i == 0:    
                if arr[j] == 0:
                    arr[j] = 1
                else:
                    arr[j] = 0
    print(arr.count(0) - 1)