T = int(input())
for t in range(T):
    num = input()
    cnt = 0
    while True:
        if num == '6174':
            print(cnt)
            break
        else:
            num = ' '.join(num).split()
            num.sort()
            a = ''
            b = ''
            for i in range(len(num)):
                a += num[i]
                b += num[-(i + 1)]
            num_lst = [int(a), int(b)]
            num = str(max(num_lst) - min(num_lst))
            if len(num) < 4:
                for i in range(4 - len(num)):
                    num += '0'
            cnt += 1

