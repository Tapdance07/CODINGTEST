def solution(n, m, section):
    answer = 0
    curr_paint = 0
    
    for s in section:
        if s > curr_paint:
            curr_paint = s + m - 1
            answer += 1
            
    return answer