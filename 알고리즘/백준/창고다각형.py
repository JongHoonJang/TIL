N = int(input())
building = {}
for n in range(N):
    l, h = map(int, input().split())
    building[l] = h
i = 0
result = []
arr = []
if N > 1:
    while i < max(building.keys()):
        if i in building.keys():
            if len(result) == 0 or result[-1][-1] <= building.get(i):
                result.append([i, building.get(i)])
                i += 1
            else:
                i += 1
        else:
            i += 1
    while i > 0:
        if i in building.keys():
            if len(arr) == 0 or arr[-1][-1] < building.get(i):
                arr.append([i, building.get(i)])
                i -= 1
            else:
                i -= 1
        else:
            i -= 1
    value = 0
    for j in range(len(result)):
        if j == len(result) - 1:
            if arr[-1][-1] == result[j][1]:
                value += (((arr[-1][-2] + 1) - result[j][0]) * result[j][1])
            else:
                value += (((arr[-1][-2]) - result[j][0]) * result[j][1])
        else:
            value += ((result[j+1][0] - result[j][0]) * result[j][1])
    if len(arr) == 1 and arr[-1][-1] != result[len(result) - 1][1]:
        value += arr[0][1]
    else:
        for j in range(len(arr) - 1):
            value += ((arr[j][0] - arr[j+1][0]) * arr[j][1])

if N == 1:
    print(h)
else:
    print(value)
