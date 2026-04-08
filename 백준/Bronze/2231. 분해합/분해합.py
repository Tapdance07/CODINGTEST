N = int(input())
T = list(str(N))

def splitNum(n):
    answer = n
    for z in range(len(T), -1,-1):
        answer += n // 10**z
        n = n%10**z
    return answer

result = 0
for i in range(1,N,1):
    if N == splitNum(i):
        result = i
        break
print(result)