def solution(arr):
    
    mins = min(arr)
    
    arr.remove(mins)
    

    if len(arr) == 0:
        return [-1]
    
    return arr