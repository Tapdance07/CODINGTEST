S = input()
T = [0]*26
for i in range(len(S)):
    T[ord(S[i].upper())-65] +=1

if T.count(max(T)) > 1:
    print("?")
else:
    print(chr(T.index(max(T))+65).upper())
