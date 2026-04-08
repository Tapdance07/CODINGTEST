import sys

n = int(sys.stdin.readline().rstrip())
ent =  set()

for i in range(n):
    A,B = sys.stdin.readline().rstrip().split()
    if B == 'enter':
        ent.add(A)
    else:
        ent.remove(A)

listEnt = list(ent)
listEnt.sort(reverse=True)
for i in listEnt:
    print(i)
