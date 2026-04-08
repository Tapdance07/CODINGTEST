import sys
input = sys.stdin.readline

N = int(input())
San = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    T, P = San[i]
    if i + T <= N:
        dp[i] = max(P + dp[i + T], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])