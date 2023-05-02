import sys
from collections import deque
N = int(input())
lst = deque()
for i in range(N):
    que = sys.stdin.readline().split()
    if que[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            ans = lst.popleft()
            print(ans)
    elif que[0] == 'size':
        print(len(lst))
    elif que[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif que[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif que[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif que[0] == 'push':
        lst.append(int(que[1]))