import sys

# 입력 읽기
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

# 분수 더하기
numerator = A[0] * B[1] + A[1] * B[0]  # 결과 분자
denominator = A[1] * B[1]              # 결과 분모

# 최대공약수 구하기
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 약분하기
g = gcd(numerator, denominator)
numerator //= g
denominator //= g

# 결과 출력
print(numerator, denominator)
