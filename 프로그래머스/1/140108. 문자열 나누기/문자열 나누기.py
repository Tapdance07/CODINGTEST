def solution(s):
    answer = 0
    x = s[0]
    xc = 0
    nxc = 0
    for i in range(len(s)):
        if x == s[i]:
            xc += 1
        else:
            nxc += 1
        if i < len(s)-1:
            if xc == nxc:
                answer += 1
                x = s[i+1]
        else:
             answer += 1 
    return answer