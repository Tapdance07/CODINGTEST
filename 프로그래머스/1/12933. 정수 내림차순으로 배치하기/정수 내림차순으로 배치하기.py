def solution(n):
    sorted_list = sorted(str(n), reverse=True)
    answer = int(''.join(sorted_list))
    
    return answer