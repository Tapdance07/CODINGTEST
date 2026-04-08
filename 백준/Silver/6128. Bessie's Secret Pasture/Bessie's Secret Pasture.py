import sys

def solve():
    n = int(sys.stdin.readline())
    
    # dp[k][s]: k개의 제곱수를 사용하여 합 s를 만드는 경우의 수
    # k는 1부터 4까지 필요함
    dp = [0] * (n + 1)
    dp[0] = 1 # 초기값: 0개로 합 0을 만드는 경우 1가지
    
    # 최종 결과를 저장할 변수 (4개를 골랐을 때의 합이 n인 경우)
    final_count = [0] * (n + 1)
    
    # 4번 반복 (정확히 4개의 숫자를 고름)
    # 하지만 0을 포함하므로 '최대 4개'가 아닌 '정확히 4개'의 루프를 관리
    current_dp = [0] * (n + 1)
    current_dp[0] = 1
    
    # 4개의 숫자를 하나씩 추가하며 DP 갱신
    # 각 단계(1개 선택, 2개 선택...)마다 가능한 제곱수를 모두 더해줌
    # 결과적으로 4회 반복 후 dp[n]이 답이 됨
    
    res_dp = [0] * (n + 1)
    res_dp[0] = 1
    
    for _ in range(4):
        next_dp = [0] * (n + 1)
        for i in range(int(n**0.5) + 1):
            square = i * i
            for j in range(square, n + 1):
                next_dp[j] += res_dp[j - square]
        res_dp = next_dp

    print(res_dp[n])

solve()