def solution(food):
    forward = ''
    backward = ''
    for i in range(1,len(food)):
        forward = forward + (str(i) * (food[i]//2))
    backward = forward[::-1]
    forward += '0'
    forward = forward + backward
    return forward