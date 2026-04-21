def solution(s):
    answer = []
    dict = {}
    for i, char in enumerate(s):
        if char not in dict:
            answer.append(-1)
        else:
            answer.append(i - dict[char])
        dict[char] = i
        
        
        
        
    return answer