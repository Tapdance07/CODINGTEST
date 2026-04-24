def solution(name, yearning, photo):
    answer = []
    for photos in photo:
        result = []
        for i,n in enumerate(name):
            if n in photos:
                result.append(yearning[i])
        answer.append(sum(result))
    
    return answer