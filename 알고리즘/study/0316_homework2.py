import sys
sys.stdin = open("중위순회_input.txt")


def inorder(n):
    if n <= N:
        inorder(n*2)
        print(alpha[n], end="")
        inorder(n*2+1)


for t in range(1, 11):
    N = int(input())
    alpha = [''] * (N + 1)
    word = [input().split() for _ in range(N)]
    for w in word:
        alpha[int(w[0])] = w[1]
    print(f'#{t} ', end="")
    inorder(1)
    print()
