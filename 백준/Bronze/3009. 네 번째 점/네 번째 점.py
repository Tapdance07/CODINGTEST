A = list()
B = list()

for i in range(3):
    C, D = map(int,input().split())
    if C not in A:
        A.append(C)
    else:
        A.remove(C)

    if D not in B:
        B.append(D)
    else:
        B.remove(D)
A.append(B[0])
print(*A)