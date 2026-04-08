n = int(input())
# def MenOfPassion(A,n):
#     sum = 0
#     for i in range(1,n):
#         for j in range(i+1,n):
#             sum = sum + A[i] * A[j]
#     return sum
#
if n ==1:
    print(0)
else:
    print(n*(n-1)//2)
print(2)