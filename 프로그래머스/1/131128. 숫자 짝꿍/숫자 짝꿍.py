def solution(X, Y):
    count_x = {str(n): 0 for n in range(10)}
    count_y = {str(n): 0 for n in range(10)}
    
    for char in X:
        count_x[char] += 1
    for char in Y:
        count_y[char] += 1
        
    result = []
    
    for i in range(9, -1, -1):
        digit = str(i)
        common_count = min(count_x[digit], count_y[digit])
        result.append(digit * common_count)
    
    answer = ''.join(result)
    
    if not answer:               
        return "-1"
    if answer[0] == "0":
        return "0"
        
    return answer