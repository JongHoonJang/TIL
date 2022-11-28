def inorder(n):
    global value
    if n <= N:
        inorder(n * 2)
        node[n] = value
        value += 1
        inorder(n * 2 + 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    node = [0] * (N + 1)
    value = 1
    inorder(1)
    print(f'#{t} {node[1]} {node[N // 2]}')
