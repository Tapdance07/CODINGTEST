import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    TN = [1,1,1,2,2]
    N = int(sys.stdin.readline().rstrip())
    if N < 6:
        print(TN[N-1])
    else:
        for i in range(6,N+1):
            TN.append(TN[i-2]+TN[i-6])
        print(TN[-1])