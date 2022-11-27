import sys
sys.stdin = open("0225_input.txt")

for t in range(0, 10):
    tc = int(input())
    numbers = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            if numbers[0] - i <= 0:
                numbers.pop(0)
                numbers.append(0)
                break
            else:
                numbers.append(numbers.pop(0) - i)
        if 0 in numbers:
            break

    print(f'#{tc}', *numbers)

