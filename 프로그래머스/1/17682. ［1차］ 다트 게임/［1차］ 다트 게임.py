def solution(dartResult):
    result = []
    temp = ''  

    for dart in dartResult:
        if dart.isdigit():
            temp += dart
        elif dart in ['S', 'D', 'T']:
            point = int(temp)
            temp = '' 
        
            if dart == 'D':
                point = point ** 2
            elif dart == 'T':
                point = point ** 3
            result.append(point)
        elif dart == '*':
            result[-1] *= 2
            if len(result) > 1:
                result[-2] *= 2
        elif dart == '#':
            result[-1] *= -1
        
    return (sum(result))