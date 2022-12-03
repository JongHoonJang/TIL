num = int(input())
i = 0
count = 0
result = []
while i < num:
    cnt = 0
    num_lst = [num, num - i]
    for j in range(30000):
        if num_lst[-2] - num_lst[-1] >= 0:
            num_lst.append(num_lst[-2] - num_lst[-1])
        else:
            cnt = len(num_lst)
            i += 1
            break
    if count < cnt:
        count = cnt
        result = num_lst
else:
    print(count)
    print(' '.join([str(result[k]) for k in range(len(result))]))