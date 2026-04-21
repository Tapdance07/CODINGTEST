def solution(sizes):
    mins = 0
    maxs = 0
    for w,h in sizes:
        big = max(w,h)
        small = min(w,h)
        
        if big > maxs:
            maxs = big
        if small > mins:
            mins = small
    return maxs * mins