w, h = map(int,input().split())
cuting = int(input())
lst = [[0] for _ in range(2)]
for i in range(cuting):
    xy, num = map(int, input().split())
    lst[xy].append(num)
lst[0].append(h)
lst[1].append(w)
lst[0].sort()
lst[1].sort()
w_lst = []
h_lst = []
for i in range(len(lst[0]) - 1, 0, -1):
    h_lst.append(lst[0][i] - lst[0][i - 1])
for i in range(len(lst[1]) - 1, 0, -1):
    w_lst.append(lst[1][i] - lst[1][i - 1])

print(max(h_lst) * max(w_lst))