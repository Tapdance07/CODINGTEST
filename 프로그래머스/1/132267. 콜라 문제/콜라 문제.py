def solution(a, b, n):
    answer = 0
    while n >= a:
        new, r = divmod(n,a)
        n = b * new + r
        answer += (b * new)
    return answer