def solution(s):
    answer = True
    s = s.upper()
    s = list(s)
    P = s.count('P')
    Y = s.count('Y')
    if P == Y:
        answer = True
    else:
        answer = False
    
    

    return answer