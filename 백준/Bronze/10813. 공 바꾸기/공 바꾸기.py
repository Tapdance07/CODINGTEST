N,M = map(int, input().split())
b = [0] * N
ba = [0]

for z in range(N):
    b[z]=z+1

for z in range(M):
    i,j = map(int,input().split())
    ba[0] = b[i-1]
    b[i-1] = b[j-1]
    b[j-1] = ba[0]
print(*b)