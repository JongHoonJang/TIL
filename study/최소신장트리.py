import sys
sys.stdin = open("최소신장트리_input.txt")
# Prim
# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [[0]*(N + 1) for _ in range(N+1)]
#     for i in range(M):
#         s, e, num = map(int, input().split())
#         arr[s][e] = num
#         arr[e][s] = num
#     key = [9999999] * (N + 1)
#     visited = [0] * (N + 1)
#     key[0] = 0
#     cnt = 0
#     while cnt < N:
#         min_value = 9999999
#         for i in range(N + 1):
#             if not visited[i] and key[i] < min_value:
#                 min_value = key[i]
#                 u = i
#         visited[u] = 1
#         for w in range(N + 1):
#             if arr[u][w] > 0 and not visited[w]:
#                 if key[w] > arr[u][w]:
#                     key[w] = arr[u][w]
#         cnt += 1
#     print(f'#{t} {sum(key)}')

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    # 가중치 오름차순 정렬
    arr.sort(key=lambda x: x[2])
    # 대표 원소 => make_set
    parent = list(range(V + 1))

    # 대표 노드 찾기
    def find_set(node):
        if node == parent[node]:
            return node
        else:
            return find_set(parent[node])


    def mst():
        count = 0

        total_value = 0
        # 0 ~ E-1
        i = 0
        while count < V:
            # 각 노드별 대표 노드
            p1 = find_set(arr[i][0])
            p2 = find_set(arr[i][1])

            # 대표 노드가 다르면 => 다른 그룹이다
            if p1 != p2:
                # union
                parent[p2] = p1
                # 가중치 누적
                total_value += arr[i][2]
                count += 1
            i += 1
        return total_value
    res = mst()
    print(f'#{t} {res}')
