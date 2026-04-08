import sys

def solve():
    # 도시의 개수 입력
    n = int(sys.stdin.readline())
    
    # 인접한 도시 사이의 거리 (n-1개)
    distances = list(map(int, sys.stdin.readline().split()))
    
    # 각 도시의 주유소 가격 (n개)
    prices = list(map(int, sys.stdin.readline().split()))
    
    # 초기 설정
    total_cost = 0
    # 첫 번째 도시의 가격을 초기 최소 가격으로 설정
    min_price = prices[0]
    
    for i in range(n - 1):
        # 현재까지 지나온 도시 중 기름값이 가장 싼 곳을 선택
        if prices[i] < min_price:
            min_price = prices[i]
        
        # 선택된 가장 싼 가격으로 다음 도시까지의 거리만큼 주유
        total_cost += min_price * distances[i]
        
    print(total_cost)

solve()