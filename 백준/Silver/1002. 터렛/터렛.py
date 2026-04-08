import sys
import math

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    Ts = list(map(int, sys.stdin.readline().rstrip().split()))
    d = math.sqrt((Ts[0] - Ts[3])**2 + (Ts[1] - Ts[4])**2)
    r1 = Ts[2]
    r2 = Ts[5]

 
    if d == 0 and r1 == r2:
        print(-1)
   
    elif d == abs(r1 - r2) or d == r1 + r2:
        print(1)
    
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    
    else:
        print(0)
