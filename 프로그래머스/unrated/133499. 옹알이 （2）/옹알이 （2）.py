def solution(babbling):
    answer = 0
    say = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        r = ''
        while True:
            if len(b) == 0:
                answer += 1
                break
            elif b[:2] in say:
                if r == b[:2]:
                    break
                r = b[:2]
                b = b[2:]
            elif b[:3] in say:
                if r == b[:3]:
                    break
                r = b[:3]
                b = b[3:]
            else:
                break
        
    return answer