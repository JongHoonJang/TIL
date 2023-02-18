A = int(input())
B = int(input())
C = int(input())
res = str(A * B * C)
arr = [0] * 10
for i in res:
    arr[int(i)] += 1
for a in arr:
    print(a)
