import sys

sys.stdin = open("회문_input.txt")


def is_palin(txt):
    start = 0
    end = len(txt) - 1
    while start <= end:
        if txt[start] != txt[end]:
            return False
        start += 1
        end -= 1
    else:
        return True


def find_word(words, n, m):
    for i in range(len(words)):
        for dj in range(n - m + 1):
            text = ''
            for j in range(m):
                text += words[i][j + dj]
            print(text)
            if is_palin(text):
                return text


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    word = [input() for _ in range(N)]
    result = ''
    for i in range(N):
        new_word = ''
        for j in range(N):
            new_word += word[j][i]
        word.append(new_word)
    print(word)
    result = find_word(word, N, M)

    # for i in range(len(word)):
    #     for j in range(N - M + 1):
    #         cnt = 0
    #         for k in range(M // 2):
    #             if word[i][j + k] == word[i][M + j - k - 1]:
    #                 cnt += 1
    #         if cnt == M // 2:
    #             result = word[i][j:j + M]

    # for i in range(len(word)):
    #     for j in range(N - M + 1):
    #         if word[i][j:j+M] == ''.join(reversed(word[i][j:j+M])):
    #             result = word[i][j:j+M]
    print(f'#{t} {result}')
