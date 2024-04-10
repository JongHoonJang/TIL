def solution(age):
    ans = ''
    for a in [str(chr(int(i) + 97)) for i in str(age)]:
        ans += a
    return ans