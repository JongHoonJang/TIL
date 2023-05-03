import sys

N = int(sys.stdin.readline())

card = [i for i in range(1, N + 1)]

while True:
    print(card.pop(0), end=' ')
    if len(card) != 0:
        card.append(card.pop(0))
    else:
        break
    
