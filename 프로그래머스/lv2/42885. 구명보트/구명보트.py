def solution(people, limit):
    answer = 0
    people.sort()                
    s = 0
    e = len(people) - 1
    while s <= e:               
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:                     
            e -= 1
        answer += 1
    return answer