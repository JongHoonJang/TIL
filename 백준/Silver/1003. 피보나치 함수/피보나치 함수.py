import sys
input = sys.stdin.readline
zero=[0]*42
one=[0]*42
zero[0]=1
one[1]=1
t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        zero[j+2]=zero[j+1]+zero[j]
        one[j+2]=one[j+1]+one[j]
    print(zero[n],one[n],sep=' ')