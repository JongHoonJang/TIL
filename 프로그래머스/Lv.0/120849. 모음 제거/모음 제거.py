def solution(my_string):
    for s in ['a', 'e', 'i', 'o', 'u']:
        my_string = my_string.replace(s, '')
    return my_string