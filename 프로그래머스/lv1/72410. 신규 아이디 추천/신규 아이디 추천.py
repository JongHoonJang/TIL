def solution(new_id):
    lst = ['0','1','2','3','4','5','6','7','8','9','-','_','.']
    # 1단계
    new_id = new_id.lower()
    # print(new_id, 1)
    # 2단계
    for d in new_id:
        if 97 <= ord(d) < 123 or d in lst:
            continue
        else:
            new_id = new_id.replace(d,'')
    # print(new_id, 2)
    # 3단계
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    # print(new_id, 3)
    # 4단계
    new_id = new_id.strip('.')
    # print(new_id, 4)
    # 5단계
    if new_id == '':
        new_id = 'a'
    # print(new_id, 5)
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    # print(new_id, 6)
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    # print(new_id, 7)
    return new_id