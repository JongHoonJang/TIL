import sys
a=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))

def chat(target,m):
    start=0
    end=len(m)-1
    while start<=end:
        mid=(start+end)//2
        if target==m[mid]:
            return 1
        elif target<m[mid]:
            end=mid-1
        else:
            start=mid+1
    return 0

b=int(sys.stdin.readline())
x=list(map(int,sys.stdin.readline().split()))
m.sort()
for i in x:
    print(chat(i,m))