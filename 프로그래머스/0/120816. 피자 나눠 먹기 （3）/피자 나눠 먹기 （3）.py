def solution(slice, n):
    if n % slice:
        return n // slice + 1
    return n // slice