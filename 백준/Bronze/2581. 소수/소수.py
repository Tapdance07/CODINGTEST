M = int(input())
N = int(input())
A = list()
for i in range(M, N + 1):
    if i > 1: 
        is_prime = True
        for z in range(2, int(i**0.5) + 1):  
            if i % z == 0:
                is_prime = False
                break
        if is_prime:
            A.append(i)

if len(A) == 0:
    print(-1)
else:
    print(sum(A))
    print(min(A))
