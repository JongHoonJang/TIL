import sys

sys.stdin = open("electric_bus_input.txt")
T = int(input())

for t in range(1, T + 1):
    K, N, M = list(map(int, input().split())) # K = 최대이동거리 N = 정류장 개수, M = 충전소개수
    charging = list(map(int, input().split())) # 충전소 위치를 리스트로 받아옴
    count = bus = 0 # 충전횟수랑 버스위치 초기화화
    # 버스위치+이동거리가 정류장수보다 작을때 동작
    while bus + K < N:
        # 최대 이동거리
        for move in range(K, 0, -1):
            # 만약 버스위치+이동거리가 충전소 위치에 있으면
            if bus + move in charging:
                bus += move
                count += 1
                break # for문 종료
        # for문이 끝까지 돌아갔을경우 버스위치+이동거리에 충전소가 없을경우
        else:
            count = 0
            break

    print(f'#{t} {count}')
