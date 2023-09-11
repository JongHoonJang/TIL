import copy
def solution(expression):
    answer = 0
    opers = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    expression = expression.replace('*', ' * ')
    expression = list(expression.split())
    for oper in opers:
        i = 0
        ex = copy.deepcopy(expression)
        while i < 3:
            idx = 0
            while oper[i] in ex:
                if ex[idx] == oper[i]:
                    if oper[i] == '+':
                        ex[idx - 1] = int(ex[idx - 1]) + int(ex[idx + 1])
                        del ex[idx:idx + 2]
                        idx = 0
                    elif oper[i] == '-':
                        ex[idx - 1] = int(ex[idx - 1]) - int(ex[idx + 1])
                        del ex[idx:idx + 2]
                        idx = 0
                    elif oper[i] == '*':
                        ex[idx - 1] = int(ex[idx - 1]) * int(ex[idx + 1])
                        del ex[idx:idx + 2]
                        idx = 0
                if idx < len(ex) - 1:
                    idx += 1
            i += 1
        if ex[0] < 0:
            ex[0] *= -1
        if answer < ex[0]:
            answer = ex[0]
    return answer