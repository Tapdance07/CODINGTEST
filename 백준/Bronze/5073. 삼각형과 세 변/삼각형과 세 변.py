while True:
    A = list(map(int,input().split()))
    if sum(A)==0:
        break
    if A.count(A[0]) == 3:
        print("Equilateral")
    else:
        if max(A) >= sum(A)-max(A):
            print("Invalid")
        else:
            if A.count(A[0]) ==2 or A.count(A[1]) ==2:
                print("Isosceles")
            else:
                print("Scalene")
