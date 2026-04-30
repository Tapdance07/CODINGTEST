def solution(keymap, targets):
    answer = []
    char_min_press = {}
    
    for key in keymap:
        for i, char in enumerate(key):
            press_count = i + 1
            
            if char not in char_min_press or press_count < char_min_press[char]:
                char_min_press[char] = press_count
    
    for target in targets:
        total_press = 0
        for char in target:
            if char in char_min_press:
                total_press += char_min_press[char]
            else:
                total_press = -1
                break
        answer.append(total_press)
        
    return answer