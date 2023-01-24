arr = []
for i in range(5):
    arr.append(int(input()))
    
if sum(arr) % 5:
    print(sum(arr) // 5 + 1)
else:
    print(sum(arr) // 5)
arr.sort()
print(arr[2])