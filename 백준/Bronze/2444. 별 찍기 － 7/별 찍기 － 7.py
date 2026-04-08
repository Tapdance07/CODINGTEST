N = int(input())
for i in range(2*N-1):
    if i <= (N-1):
        print(' '*(N-i-1)+"*"*(i*2+1))
    elif i > (N-1):
       print(' '*(i-N+1)+"*"*(2*((2*N-1)-i)-1))