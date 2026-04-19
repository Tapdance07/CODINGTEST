def solution(arr, divisor):
    answer = sorted([a for a in arr if a % divisor == 0])
    
    return answer if len(answer) > 0 else [-1]