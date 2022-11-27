import sys

sys.stdin = open("card_input.txt")
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cards = input()
    number = count = 0
    new_card = []

    new_card = [int(card) for card in cards]
    number = new_card[0]
    count = new_card.count(new_card[0])
    for i in range(1, n):
        if new_card.count(new_card[i]) > count:
            number = new_card[i]
            count = new_card.count(new_card[i])
        elif new_card.count(new_card[i]) == count:
            if number < new_card[i]:
                number = new_card[i]

    print(f'#{t} {number} {count}')





