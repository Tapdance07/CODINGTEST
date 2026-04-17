def solution(n):
    answer = -1
    
    for i in range(n+1):
        if (i**2) == n:
            answer = (i+1)**2
            break
        

    return answer