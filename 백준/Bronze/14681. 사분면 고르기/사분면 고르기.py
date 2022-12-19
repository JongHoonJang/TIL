lst = [int(input()) for _ in range(2)]

if lst[0] < 0 and lst[1] < 0:  
    print(3)
elif lst[0] < 0 and lst[1] > 0:
    print(2)
elif lst[0] > 0 and lst[1] > 0:
    print(1)
else:
    print(4)