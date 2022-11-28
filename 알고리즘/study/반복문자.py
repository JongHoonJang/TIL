import sys
sys.stdin = open("반복문자_input.txt")


def str_set(x):
    for i in range(len(x) - 1): # 0~문장의 길이 - 1 까지
        if x[i] == x[i + 1]: #x[i]가 x[i+1]과 같을 경우
            # x.pop(i)를 두번하는데 똑같은 인덱스를 두번 pop매서드 이용해야
            # x[i]와 x[i + 1] 삭제 가능
            # ex) ABCCB -> x[2] == x[3]
            # x.pop(2) -> ABCB
            # x.pop(2) -> ABB
            x.pop(i)
            x.pop(i)
            # 재귀함수
            return str_set(x)
    else: # 반복문이 다돌아가면 = 반복문자가 없을경우
        return len(x) # x의 길이를 반환


T = int(input())

for t in range(1, T + 1):
    string = input() # 문장을 받아와서
    lst_s = [] # 빈 리스트 생성
    for s in string: # 문장의 알파벳 하나하나를 빈 리스트에 추가
        lst_s.append(s)

    print(f'#{t} {str_set(lst_s)}')
