def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI',"SAT",'SUN','MON',"TUE",'WED','THU']
    k = 0
    answer = ''
    if a == 1:
        k = b % 7
        answer = weeks[k - 1]
    else :
        for i in range(a - 1) :
            k += days[i]
        k += b
        k %= 7
        answer = weeks[k - 1]

    return answer