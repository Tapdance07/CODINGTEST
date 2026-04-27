def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for s in speak:
            if s * 2 in word:
                break
            
            word = word.replace(s, ' ')
            
        if word.rstrip() =='':
            answer += 1
            
            
            
    return answer