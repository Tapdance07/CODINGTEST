import sys

# 입력 받기
n = int(sys.stdin.readline().strip())


dp = [0] * (n + 1)

# 초기값 설정
dp[1] = 1
if n > 1:
    dp[2] = 3

# 점화식에 따라 DP 값 계산
for i in range(3, n + 1):
    if i%2 == 0:
        dp[i] = (dp[i-1]*2 +1) % 10007
    else:
        dp[i] = (dp[i - 1] * 2 -1) % 10007

print(dp[n])