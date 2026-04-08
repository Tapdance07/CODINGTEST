N , M = map(int,input().split())
T = list(map(int,input().split()))

A = list()

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if T[i]+T[j]+T[k] <= M:
                A.append(T[i]+T[j]+T[k])


print(max(A))
