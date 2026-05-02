def solution(lottos, win_nums):
    zero_num = lottos.count(0)  
    match_num = 0
    
    for num in lottos:
        if num in win_nums:
            match_num += 1
            

    
    high = 7 - (match_num + zero_num)
    low = 7 - match_num
    
    if high > 6: high = 6
    if low > 6: low = 6
    
    return [high, low]