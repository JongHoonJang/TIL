T = int(input())
for t in range(1, T + 1):
    cards = list(map(int, input().split()))
    result = '0'
    brk = 0
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(12):
        if i % 2:
            player2[cards[i]] += 1
        else:
            player1[cards[i]] += 1
        if i > 4:
            for j in range(10):
                if player1[j] == 3:
                    result = '1'
                    brk = 1
                    break
                if player2[j] == 3:
                    result = '2'
                    brk = 1
                    break
                if j < 8:
                    if 0 not in player1[j:j + 3]:
                        result = '1'
                        brk = 1
                        break
                    if 0 not in player2[j:j + 3]:
                        result = '2'
                        brk = 1
                        break
        if brk == 1:
            break
    print(f'#{t} {result}')
