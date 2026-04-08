N,K = map(int,input().split())
A =list()
A.append(1)
for i in range(2,N+1):

    if N % i == 0:
        A.append(i)

if len(A)>=K:
    print(A[K-1])
else:
    print(0)