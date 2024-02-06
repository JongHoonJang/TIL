def dictionary():
    dic = {}
    cnt = 1
    text = 'A'
    dnext = {}
    dnext['A'] = 'E'
    dnext['E'] = 'I'
    dnext['I'] = 'O'
    dnext['O'] = 'U'
    dic[text] = cnt
    while True:
        if text == 'UUUUU':
            break

        cnt += 1

        if len(text) < 5:
            text = text + 'A'

        elif len(text) == 5:
            if text[4] != 'U':
                text = text[0:4] + dnext[text[4]]

            else:
                if text[3] == 'U':
                    if text[2] == 'U':
                        if text[1] == 'U':
                            text = dnext[text[0]]
                        else:
                            text = text[0] + dnext[text[1]]
                    else: 
                        text = text[0:2] + dnext[text[2]]
                else:
                    text = text[0:3] + dnext[text[3]]
        dic[text] = cnt   
        
    return dic


def solution(word):
    answer = 0

    dic = dictionary()
    answer = dic[word]

    return answer