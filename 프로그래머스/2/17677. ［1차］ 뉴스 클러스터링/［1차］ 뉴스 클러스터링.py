def solution(str1, str2):
    answer = 65536
    str1 = str1.upper()
    str2 = str2.upper()
    str_lst1 = []
    str_lst2 = []
    nlst = []
    ulst = []
    for i in range(len(str1) - 1):
        if 64 < ord(str1[i]) < 91 and 64 < ord(str1[i + 1]) < 91:
            str_lst1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if 64 < ord(str2[i]) < 91 and 64 < ord(str2[i + 1]) < 91:
            str_lst2.append(str2[i:i + 2])

    while True:
        if str_lst1 == [] and str_lst2 == []:
            break
        elif str_lst1 == []:
            ulst.extend(str_lst2)
            break
        elif str_lst2 == []:
            ulst.extend(str_lst1)
            break
        s = str_lst1.pop()
        if s in str_lst2:
            str_lst2.pop(str_lst2.index(s))
            nlst.append(s)
        ulst.append(s)
    if ulst == [] and nlst == []:
        return answer
    return int(answer * (len(nlst) / len(ulst)))