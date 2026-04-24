def solution(number, limit, power):
    total_weight = 0
    
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j * j == i: 
                    count += 1
                else:          
                    count += 2
            
            if count > limit:
                break
        
        if count > limit:
            total_weight += power
        else:
            total_weight += count
            
    return total_weight