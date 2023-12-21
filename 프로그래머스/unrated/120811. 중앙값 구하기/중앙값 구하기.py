def solution(array):
    array.sort()
    if len(array) % 2:
        return array[len(array) // 2]
    return array[len(array) // 2 - 1]
    