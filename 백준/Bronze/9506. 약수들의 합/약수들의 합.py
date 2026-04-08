while 1:
    n = int(input())
    A = list()
    if n == -1:
        break
    else:
        for i in range(1,n):
            if (n%i)==0:
                A.append(i)
            else:
                pass
        if sum(A) == n:
            print(f"{n} = {A[0]}",end='')

            for i in range (1,len(A)):
                print(" +",A[i],end='')


        else:
            print(f"{n} is NOT perfect.",end='')
        print()
