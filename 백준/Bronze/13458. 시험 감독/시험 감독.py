import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

total = 0

for i in range(N):
    # 총감독관 1명은 반드시 배치
    total += 1
    remaining = A[i] - B
    
    if remaining > 0:
        # 부감독관 수는 남은 인원을 부감독관이 커버할 수 있는 인원수로 나눈 값
        total += remaining // C
        if remaining % C != 0:
            total += 1

print(total)