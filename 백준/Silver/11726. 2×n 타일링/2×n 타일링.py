import sys

# 입력 받기
n = int(sys.stdin.readline().strip())


dp = [0] * (n + 1)

# 초기값 설정
dp[1] = 1
if n > 1:
    dp[2] = 2

# 점화식에 따라 DP 값 계산
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007


print(dp[n])