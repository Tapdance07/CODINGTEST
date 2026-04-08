N = int(input())

if N == 1:
    print(1)
else:
    # 변수 두 개로 이전 값들을 관리
    prev2 = 1 # dp[i-2] 역할
    prev1 = 1 # dp[i-1] 역할
    
    for i in range(2, N + 1):
        # 매번 15746으로 나누어 숫자가 커지는 것을 방지
        current = (prev1 + prev2) % 15746
        prev2 = prev1
        prev1 = current
        
    print(prev1)