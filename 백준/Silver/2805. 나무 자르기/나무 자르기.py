N, M = map(int, input().split())
trees = list(map(int, input().split()))
s = 0
e = max(trees)
while s <= e:
    mid = (s + e) // 2
    res = 0
    for i in trees:
        if i >= mid:
            res += (i - mid)

    if res >= M:
        s = mid + 1
    else:
        e = mid - 1
        
print(e)