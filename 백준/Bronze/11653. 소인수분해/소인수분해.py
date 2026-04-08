N = int(input())
A = list()
if N == 1:
    pass
else:
    i = 2
    while N != 1:
        if N % i == 0:
            print(i)
            A.append(i)
            N /= i
        else:
            i += 1

