def solution(numbers):
    answer = []
    diff = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            diff.add(numbers[i] + numbers[j])
    
    answer = list(diff)
    return sorted(answer)