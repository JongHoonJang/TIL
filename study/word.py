import sys

sys.stdin = open("word_input.txt")
T = int(input())

for t in range(1,  T + 1):
    str1 = input()
    str2 = input()
    max_cnt = 0
    max_word = ''
    for word in set(str1):
        cnt = 0
        for i in range(len(str2)):
            if word == str2[i]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{t} {max_cnt}')
