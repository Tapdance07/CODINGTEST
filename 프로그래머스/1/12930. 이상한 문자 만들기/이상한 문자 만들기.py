def solution(s):
    words = s.split(' ') 
    new_words = []
    
    for word in words:
        converted = ""
        for i in range(len(word)):
            if i % 2 == 0: 
                converted += word[i].upper()
            else:          
                converted += word[i].lower()
        new_words.append(converted)
        
    return ' '.join(new_words)