def solution(myString):
    myString = myString.split('x')
    
    return [len(s) for s in myString]