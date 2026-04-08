N,M = map(int,input().split())
b = [0] * N
for S in range(M):
    i,j,k = map(int,input().split())
    for z in range(i-1,j):
        b[z] = k
print(*b)
