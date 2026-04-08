S = input()
for i in range(len(S)):
    if len(S) ==1:
        print(1)
    if S[i] == S[-i-1]:
        if i == ((len(S) // 2)-1):
            print(1)
            break
    else:
        print(0)
        break