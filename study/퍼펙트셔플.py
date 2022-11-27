T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    stack = []
    stack2 = []
    result = []
    if N % 2:
        l = N//2 + 1
    else:
        l = N // 2
    for card in cards:
        if len(stack) == l:
            stack2.append(card)
        else:
            stack.append(card)
    for i in range(N):
        if N % 2:
            if i % 2:
                result.append(stack2.pop())
            else:
                result.append((stack.pop()))
        else:
            if i % 2:
                result.append(stack.pop())
            else:
                result.append((stack2.pop()))
    print(f'#{t}',end=' ')
    print(' '.join(result[-i] for i in range(1, N + 1)))

