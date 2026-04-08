import sys

N = int(sys.stdin.readline().rstrip())

result = (N + 1) * (N - 1) * N // 2
print(result)