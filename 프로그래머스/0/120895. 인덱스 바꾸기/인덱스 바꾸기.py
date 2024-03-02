def solution(my_string, num1, num2):
    my_string = [s for s in my_string]
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)