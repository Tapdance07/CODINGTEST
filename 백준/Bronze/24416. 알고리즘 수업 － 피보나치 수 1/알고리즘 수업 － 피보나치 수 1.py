import sys
input = sys.stdin.readline

n = int(input())

# DP로 피보나치 수 구하기
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# count_fib(n) = dp[n]
count_fib = dp[n]

# count_fibonacci = 반복문이 도는 횟수 = n - 2 (for문 i=3부터 n까지)
count_fibonacci = max(0, n - 2)

print(count_fib, count_fibonacci)
