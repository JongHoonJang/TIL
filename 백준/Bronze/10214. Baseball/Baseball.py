T = int(input())
for t in range(T):
    y = k = 0
    for i in range(9):
        Y, K = map(int, input().split())
        y += Y
        k += K
    if y > k:
        print('Yonsei')
    elif y < k:
        print('Korea')
    else:
        print('Draw')