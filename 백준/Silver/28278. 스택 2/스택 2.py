import sys
from inspect import stack

T = list()

def Stack(c):
    if c[0] == '1':
        T.append(int(c[2:]))

    elif c[0] == '2':
        if len(T)>0:
            print(T[-1])
            del T[-1]
        else:
            print(-1)
    elif c[0] == '3':
        if len(T)>0:
            print(len(T))
        else:
            print(0)
    elif c[0] == '4':
        if len(T) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == '5':
        if len(T) >0:
            print(T[-1])
        else:
            print(-1)




N = int(sys.stdin.readline().rstrip())
cmd = 0
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    Stack(cmd)


