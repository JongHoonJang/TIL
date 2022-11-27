import sys

sys.stdin = open("input.txt")
for T in range(1, 11):
    number = int(input())
    build = list(map(int, input().split()))
    best = 0
    for i in range(2, number - 2):
        view = 255 # 빌딩의 최대 높이
        #빌딩을 기준으로 양옆 2칸까지의 범위를 조사
        for v in range(5):
            if v != 2: #기준이 되는 빌딩을 제외한 나머지
                #기준이 되는 빌딩 - 범위내 빌딩 값중 최소값 구하기
                if build[i] - build[i - 2 + v] < view:
                    view = build[i] - build[i - 2 + v]
        if view > 0: #조망권이 0보다 클때
            best += view
    print(f"#{T} {best}")
