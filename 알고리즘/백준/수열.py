N = int(input())
lst = list(map(int, input().split()))
uplst = []
downlst = []
count = []
for i in range(N):
    if len(uplst) == 0 or uplst[-1] <= lst[i]:
        uplst.append(lst[i])
    elif uplst[-1] > lst[i]:
        count.append(len(uplst))
        uplst.clear()
        uplst.append(lst[i])
    if len(downlst) == 0 or downlst[-1] >= lst[i]:
        downlst.append(lst[i])
    elif downlst[-1] < lst[i]:
        count.append(len(downlst))
        downlst.clear()
        downlst.append(lst[i])
else:
    count.append(len(uplst))
    count.append(len(downlst))
print(max(count))
