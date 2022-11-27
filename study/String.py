import sys
sys.stdin = open("String_input.txt", "rt", encoding='UTF8')

for t in range(10):
    T = int(input())
    s = input()
    string = input()
    print(f'#{T} {string.count(s)}')

    count = 0
    for i in range(len(string) - 1):
        if s == string[i:i + len(s)]:
            count += 1
    print(f'#{T} {count}')
