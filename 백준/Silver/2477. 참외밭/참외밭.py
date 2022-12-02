N = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
a = []
al = []
for i in range(6):
    a.append(lst[i][0])
    al.append(lst[i][1])
for i in range(6):
    if a[0:2] == a[2:4]:
        s_box = al[1] * al[2]
        b_box = al[4] * al[5]
        print((b_box - s_box) * N)
        break
    else:
        a.append(a.pop(0))
        al.append(al.pop(0))