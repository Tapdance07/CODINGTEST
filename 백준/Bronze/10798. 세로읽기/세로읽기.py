A =list()
for i in range(5):
    A.append(list(input()))

for i in range(15):
    for z in range(5):
        try:
            if (z != 4) and (len(A[z]) <= i):
                pass
            else:
                print(A[z][i], end='')
        except:
            z +=1