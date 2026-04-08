import sys

N = int(sys.stdin.readline().rstrip())
S = set(map(int,sys.stdin.readline().rstrip().split()))
#상근이가 가지고 있는 카드


M = int(sys.stdin.readline().rstrip())
C = list(map(int,sys.stdin.readline().rstrip().split()))
#구별 할 카드

#문제 : C에 있는게 S에 있는지?

for i in range(M):
    if C[i] in S:
        print(1, end=" ")
    else:
        print(0, end=" ")
