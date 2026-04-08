T = [1, 1, 2, 2, 2, 8]
S = list(map(int, input().split())) 
for i in range(len(T)):
    T[i] = T[i] - S[i]
print(*T)
