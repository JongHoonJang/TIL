N, L = map(int, input().split())
flag = 0
remain = 0

while L <= 100:
    answer = []
    remain = 0
    flag = 1
    
    for i in range(L):
        remain += i
        
    a = (N - remain) / L
    if a>=0:
        if a % 1 != 0:
            L += 1
        else:
            for i in range(L):
                answer.append(int(a)+i)
    else:
        break   
    
    Sum = sum(answer)
    if Sum == N:
        break

if (flag) and len(answer)>0:
    answer.sort()
    for i in answer:
        print(i,end=' ')
else:    
    print(-1)