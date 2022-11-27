T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    pizza = [(i + 1, temp[i]) for i in range(M)]
    pizzas = pizza[:N]
    pizza = pizza[N:]
    while len(pizzas) != 1:
        num, cheese = pizzas.pop(0)
        cheese //= 2
        if cheese:
            pizzas.append((num, cheese))
        else:
            if pizza:
                pizzas.append(pizza.pop(0))
    num, cheese = pizzas.pop()
    print(f'#{t} {num}')
