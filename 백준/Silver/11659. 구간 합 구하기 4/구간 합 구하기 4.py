import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().rstrip().split())
N_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 누적합 배열 생성
M_list = [0] * N
M_list[0] = N_list[0]
for i in range(1, N):
    M_list[i] = M_list[i - 1] + N_list[i]

# 쿼리 처리
for _ in range(M):
    N_start, N_end = map(int, sys.stdin.readline().rstrip().split())
    if N_start == 1:
        # 시작이 1인 경우
        print(M_list[N_end - 1])
    else:
        # 일반적인 경우
        print(M_list[N_end - 1] - M_list[N_start - 2])
