N = int(input())
lst = []
for i in range(N):
    age, name = input().split()
    lst.append([int(age), name])
lst.sort(key = lambda x :(x[0]))
for i in lst:
    print(*i)