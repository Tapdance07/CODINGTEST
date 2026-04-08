import sys

N , M = map(int,sys.stdin.readline().rstrip().split())

NS = set()
MS = list()

for i in range(N):
    NS.add(sys.stdin.readline().rstrip())

for i in range(M):
    MS.append(sys.stdin.readline().rstrip())
Coun = 0
for i in MS:
    if i in NS:
        Coun += 1

print(Coun)
