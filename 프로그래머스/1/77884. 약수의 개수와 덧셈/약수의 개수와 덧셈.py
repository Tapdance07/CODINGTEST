def solution(left, right):
    
    
    return sum(-a if int(a**0.5)**2 == a else a for a in range(left,right + 1))