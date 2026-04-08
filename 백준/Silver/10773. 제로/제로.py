import sys

k = int(sys.stdin.readline().rstrip())
Q = list()
for _ in range(k):
    T = int(sys.stdin.readline().rstrip())
    if T == 0:
        del Q[-1]
    else:
        Q.append(T)
print(sum(Q))