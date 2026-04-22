def solution(array, commands):
    answer = []
    for cmd in commands:
        sliced = array[cmd[0]-1 : cmd[1]]
        
        sliced.sort()
        
        answer.append(sliced[cmd[2]-1])
    return answer