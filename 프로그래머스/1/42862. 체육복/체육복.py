def solution(n, lost, reserve):
    # 1. 정렬 (매우 중요!)
    lost.sort()
    reserve.sort()
    
    actual_reserve = [r for r in reserve if r not in lost]
    actual_lost = [l for l in lost if l not in reserve]
    
    for l in actual_lost:
        if (l - 1) in actual_reserve:
            actual_reserve.remove(l - 1)
        elif (l + 1) in actual_reserve:
            actual_reserve.remove(l + 1)
        else:
            n -= 1
            
    return n