def solution(x):
    answer = True
    
    d = sum(int(digit) for digit in str(x))
    
    if x % d:
        answer = False
    else:
        pass
    
    return answer