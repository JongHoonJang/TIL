T = int(input())
alpha = {'@':'a','[':'c','!':'i',';':'j','^':'n','0':'o','7':'t'}

for t in range(T):
    word = input()
    cnt = 0
    i = 0
    res = ''
    while True:
        if i >= len(word):
            res_l = len(res) // 2
            if len(res) % 2:
                res_l += 1
            if cnt >= res_l:
                print('I don\'t understand')
            else:
                print(res)
            break
        elif word[i:i + 3] == '\\\\\'':
            res += 'w'
            cnt += 1
            i += 3
        elif word[i:i + 2] == '\\\'':
            res += 'v'
            cnt += 1
            i += 2
        elif word[i] in alpha:
            res += alpha[word[i]]
            cnt += 1
            i += 1
        else:
            res += word[i]
            i += 1