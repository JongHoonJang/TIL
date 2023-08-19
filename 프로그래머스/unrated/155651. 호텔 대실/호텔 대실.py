def solution(book_time):
    answer = 0
    book_time.sort()
    room = []
    while book_time:
        s, e = book_time.pop(0)
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        st = sh * 60 + sm
        et = eh * 60 + em

        if len(room) == 0:
            room.append(et)
        elif room[0] + 10 > st:
            room.append(et)
        elif room[0] + 10 <= st:
            room.pop(0)
            room.append(et)
        room.sort()

        if len(room) > answer:
            answer = len(room)
            print(answer)
        
    return answer