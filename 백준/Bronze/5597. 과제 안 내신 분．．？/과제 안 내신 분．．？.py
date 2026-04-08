M = [0] * 31
for i in range(28):
    M[int(input())] = 1
for i in range(1,31):
    if M[i]==0:
        print(i)
