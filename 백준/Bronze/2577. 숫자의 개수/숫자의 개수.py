lst = [int(input()) for _ in range(3)]

num = str(lst[0]*lst[1]*lst[2])
for i in range(10):
    print(num.count(str(i)))