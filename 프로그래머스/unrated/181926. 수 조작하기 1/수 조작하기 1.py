def solution(n, control):
    return n + (control.count('w') - control.count('s')) + 10 * (control.count('d') - control.count('a'))