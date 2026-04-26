from itertools import combinations

def is_prime(n):
    """소수 판별 함수"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        current_sum = sum(comb)
        if is_prime(current_sum):
            answer += 1
            
    return answer

