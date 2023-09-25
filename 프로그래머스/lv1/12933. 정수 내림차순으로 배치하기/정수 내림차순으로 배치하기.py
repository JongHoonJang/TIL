def solution(n):
    return int(''.join(list(reversed(sorted(' '.join(str(n)).split())))))