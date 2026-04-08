import sys

# 계단 점수 입력 받기
N = int(sys.stdin.readline().rstrip())
stair = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 예외 처리: 계단이 2개 이하인 경우
if N == 1:
    print(stair[0])
    sys.exit()
elif N == 2:
    print(stair[0] + stair[1])
    sys.exit()

# DP 테이블 초기화
dp = [0] * N
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

# DP 점화식 계산
for i in range(3, N):
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

# 최댓값 출력
print(dp[-1])