def solution(myString):
    answer = []
    myString = myString.replace('x',' ')
    myString = list(myString.split())
    myString.sort()
    return myString