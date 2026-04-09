import sys
n = int(sys.stdin.readline().rstrip())

podo = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(n)]


# 연속으로 붙어있는거 3개는 못먹어
dp = [0]* (n+1)
dp[1] = podo[1]

if n>=2:
    dp[2] = podo[1] + podo[2]
    
for i in range(3,n+1):
    dp[i] = max(
            # 생략 없이 먹기
        dp[i-2] + podo[i],
        dp[i-1],
        dp[i-3] + podo[i-1] + podo[i]
        )
print(dp[n])