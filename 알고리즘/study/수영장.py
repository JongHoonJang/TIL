import sys
sys.stdin = open("swim_input.txt")

T = int(input())
for t in range(1, T + 1):
    day, month, month_3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))
    money = [0 for _ in range(13)]

    for i in range(1, 13):
        money[i] = min(swim[i] * day, month) + money[i - 1]
        if i > 2:
            money[i] = min(money[i], month_3 + money[i - 3])

    result = min(money[12], year)
    print(f'#{t} {result}')

