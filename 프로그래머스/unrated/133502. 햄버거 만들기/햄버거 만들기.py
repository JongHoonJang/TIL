
def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if len(burger) >= 4:
            if burger[len(burger) - 4:len(burger)] == [1,2,3,1]:
                del burger[len(burger) - 4:len(burger)]
                answer += 1
    return answer