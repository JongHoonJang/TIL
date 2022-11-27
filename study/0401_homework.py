import sys
sys.stdin = open("0401_input.txt")


def BFS(num, count):
    global cnt
    queue = [(num, count)]
    while queue:
        m, c = queue.pop(0)
        # 초기값을 찾으면
        if m == N:
            # cnt에 횟수 저장
            cnt = c
            return
        # 만약 홀수면
        if m % 2:
            # 나누기를 제외한 연산 실행
            # 연산된 값이 범위 내에 존재하고 한번도 방문한적이 없는 숫자면
            if 1 <= m + 1 <= 1000000 and not visited[m + 1]:
                # queue에 추가해주고
                queue.append((m + 1, c + 1))
                # 방문처리
                visited[m + 1] = 1
            if 1 <= m - 1 <= 1000000 and not visited[m - 1]:
                queue.append((m - 1, c + 1))
                visited[m - 1] = 1
            if 1 <= m + 10 <= 1000000 and not visited[m + 10]:
                queue.append((m + 10, c + 1))
                visited[m + 10] = 1
        # 짝수일경우
        else:
            # 나누기를 포함한 연산 실행
            if 1 <= m // 2 <= 1000000 and not visited[m // 2]:
                queue.append((m // 2, c + 1))
                visited[m // 2] = 1
            if 1 <= m + 1 <= 1000000 and not visited[m + 1]:
                queue.append((m + 1, c + 1))
                visited[m + 1] = 1
            if 1 <= m - 1 <= 1000000 and not visited[m - 1]:
                queue.append((m - 1, c + 1))
                visited[m - 1] = 1
            if 1 <= m + 10 <= 1000000 and not visited[m + 10]:
                queue.append((m + 10, c + 1))
                visited[m + 10] = 1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 방문처리할 리스트 생성
    visited = [0] * 1000001
    cnt = 10000000
    # 찾아야하는 숫자부터 시작
    BFS(M, 0)
    print(f'#{t} {cnt}')


# def DFS(m, c):
#     global cnt
#     if cnt <= c:
#         return
#     if m == N:
#         if cnt > c:
#             cnt = c
#         return
#     if m % 2:
#         if 1 <= m + 1 <= 1000000 and not visited[m + 1]:
#             visited[m + 1] = 1
#             DFS(m + 1, c + 1)
#             visited[m + 1] = 0
#         if 1 <= m - 1 <= 1000000 and not visited[m - 1]:
#             visited[m - 1] = 1
#             DFS(m - 1, c + 1)
#             visited[m - 1] = 0
#         if 1 <= m + 10 <= 1000000 and not visited[m + 10]:
#             visited[m + 10] = 1
#             DFS(m + 10, c + 1)
#             visited[m + 10] = 0
#     else:
#         if 1 <= m // 2 <= 1000000 and not visited[m // 2]:
#             visited[m // 2] = 1
#             DFS(m // 2, c + 1)
#             visited[m // 2] = 0
#         if 1 <= m + 1 <= 1000000 and not visited[m + 1]:
#             visited[m + 1] = 1
#             DFS(m + 1, c + 1)
#             visited[m + 1] = 0
#         if 1 <= m - 1 <= 1000000 and not visited[m - 1]:
#             visited[m - 1] = 1
#             DFS(m - 1, c + 1)
#             visited[m - 1] = 0
#         if 1 <= m + 10 <= 1000000 and not visited[m + 10]:
#             visited[m + 10] = 1
#             DFS(m + 10, c + 1)
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     cnt = 10000000
#     visited = [0] * 1000001
#     count = 0
#     if N < M:
#         DFS(M, 0)
#         print(f'#{t} {cnt}')
#     elif N > M:
#         count = (N - M) // 10
#         if (N - M) % 10 + M == 10:
#             count += 1 + M
#         else:
#             count += (N - M) % 10
#         print(f'#{t} {count}')



