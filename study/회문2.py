import sys

sys.stdin = open("회문2_input.txt")

for t in range(10):
    T = int(input())
    word = [input() for _ in range(100)]

    for i in range(100):
        new_word = ''
        for j in range(100):
            new_word += word[j][i]
        word.append(new_word)
    M = 0
    while M < 100:
        for i in range(len(word)):
            for j in range(100 - M + 1):
                cnt = 0
                for k in range(M // 2):
                    if word[i][j + k] == word[i][M + j - k - 1]:
                        cnt += 1
                    else:
                        break
                if cnt == M // 2:
                    result = word[i][j:j + M]
                    break
        M += 1
    # while M < 100:
    #     for i in range(len(word)):
    #         for j in range(100 - M + 1):
    #             if word[i][j:j+M] == ''.join(reversed(word[i][j:j+M])):
    #                 result = word[i][j:j+M]
    #                 break
    #     M += 1

    print(f'#{T} {len(result)}')


# def is_palin(txt):
#     start = 0
#     end = len(txt) - 1
#     while start <= end:
#         if txt[start] != txt[end]:
#             return False
#         start += 1
#         end -= 1
#     else:
#         return True
#
#
# def find_word(words, n, m):
#     for i in range(len(words)):
#         for dj in range(n - m + 1):
#             text = ''
#             if words[i][dj] == word[i][dj + m - 1]:
#                 for j in range(m):
#                     text += words[i][j + dj]
#                 if is_palin(text):
#                     return len(text)
#     else:
#         return find_word(words, n, m - 1)
#
#
# for t in range(10):
#     T = int(input())
#     word = [input() for _ in range(100)]
#
#     for i in range(100):
#         new_word = ''
#         for j in range(100):
#             new_word += word[j][i]
#         word.append(new_word)
#     result = find_word(word, 100, 100)
#
#     print(f'#{T} {result}')

