def solution(array, height):
    array.append(height)
    array.sort()
    array.reverse()
    return array.index(height)