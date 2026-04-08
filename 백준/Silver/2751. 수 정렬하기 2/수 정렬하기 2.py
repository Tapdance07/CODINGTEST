import sys

N = int(sys.stdin.readline())
T = list()
for i in range(N):
    T.append(int(sys.stdin.readline()))
T.sort()
for i in T:
    print(i)