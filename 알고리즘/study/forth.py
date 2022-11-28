import sys

sys.stdin = open("forth_input.txt")


def result(a, b, s):
    if s == '+':
        return b + a
    if s == '-':
        return b - a
    if s == '*':
        return b * a
    if s == '/':
        return b // a


T = int(input())

sign = ['+', '-', '/', '*']
for t in range(1, T + 1):
    forth = input().split()
    stack = []
    if forth[-1] != '.':  #맨 마지막에 '.'이 없으면 에러 출력
        print(f'#{t} error')
    else:
        forth.pop()  # '.'제거
        for f in forth:
            if f not in sign:  #숫자면 stack에 추가
                stack.append(int(f))
            else:  #기호면
                if len(stack) < 2:  # stack에 숫자 2개이상 없으면
                    print(f'#{t} error')  #에러 출력
                    break
                # stack의 길이가 2 이상이면 숫자 2개를 pop으로 꺼내 result함수로
                # 연산기호와 함께 보내고 반환된걸 다시 stack에 추가
                stack.append(result(stack.pop(), stack.pop(), f))
        else:  # 반복문이 끝나고
            if len(stack) != 1:  #stack의 길이가 1이 아니면
                print(f'#{t} error')  # 에러 출력
            else:  # 아니면
                print(f'#{t} {stack[0]}')  # 결과 출력

