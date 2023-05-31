N, M = map(int, input().split())

listen = set()
for i in range(N):
    listen.add(input())
    
look = set()
for i in range(M):
    look.add(input())

res = sorted(list(listen & look))  

print(len(res))
for r in res:
    print(r)