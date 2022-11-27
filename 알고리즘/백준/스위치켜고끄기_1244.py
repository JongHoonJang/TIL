import sys
sys.stdin = open("1244")


def not_over(a, b):
    if 0 <= a < N and 0 <= b < N:
        return True
    return False

N = int(input())
swichs = list(map(int, input().split()))
parson = int(input())
students = [list(map(int, input().split())) for _ in range(parson)]

for student in students:
    if student[0] == 1:
        for i in range(1, N + 1):
            if i % student[1] == 0:
                if swichs[i - 1]:
                    swichs[i - 1] = 0
                else:
                    swichs[i - 1] = 1
    elif student[0] == 2:
        j = 1
        idx = student[1] - 1
        if swichs[idx]:
            swichs[idx] = 0
        else:
            swichs[idx] = 1
        while not_over(idx - j, idx + j):
            if swichs[idx - j] == swichs[idx + j]:
                if swichs[idx - j]:
                    swichs[idx - j] = 0
                    swichs[idx + j] = 0
                    j += 1
                else:
                    swichs[idx - j] = 1
                    swichs[idx + j] = 1
                    j += 1
            else:
                break
else:
    for i in range(N):
        print(swichs[i], end=' ')
        if (i + 1) % 20 == 0:
            print()
