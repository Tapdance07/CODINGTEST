S = input()
Z = [-1] * 26
for i in range(len(S)):
    if Z[ord(S[i])%97] == -1:
        Z[ord(S[i])%97] = i
    else:
        pass

print(*Z)