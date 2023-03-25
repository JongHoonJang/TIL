x_lst = []
y_lst = []
for i in range(3):
    x, y = map(int, input().split())
    if x not in x_lst:
        x_lst.append(x)
    elif x in x_lst:
        x_lst.pop(x_lst.index(x))
    if y not in y_lst:
        y_lst.append(y)
    elif y in y_lst:
        y_lst.pop(y_lst.index(y))
print(x_lst[0], y_lst[0])
    