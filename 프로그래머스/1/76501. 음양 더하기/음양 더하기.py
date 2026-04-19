def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i]:
            pass
        else:
            absolutes[i] = (-absolutes[i])

    
    return sum(absolutes)