def solution(s, n):
    answer = ''
    for char in s:
        if char == " ":
            answer += " "
            continue
            
        base = ord('A') if char.isupper() else ord('a')
        shifted = (ord(char) - base + n) % 26 + base
        
        answer += chr(shifted)
            
    
    
    return answer