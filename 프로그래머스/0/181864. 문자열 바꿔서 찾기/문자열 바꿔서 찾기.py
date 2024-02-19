def solution(myString, pat):
    myString = myString.replace('A','b')
    myString = myString.replace('B','a')
    if pat.lower() in myString:
        return 1
    return 0