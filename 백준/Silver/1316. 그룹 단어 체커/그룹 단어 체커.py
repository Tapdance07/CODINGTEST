S = int(input())  
C = 0  

for _ in range(S):  
    T = input()  
    seen = set()  
    is_valid = True 

    for i in range(len(T)):
        if T[i] in seen:  
            if T[i] != T[i-1]:  
                is_valid = False
                break
        else:  
            seen.add(T[i])

    if is_valid:  
        C += 1

print(C)