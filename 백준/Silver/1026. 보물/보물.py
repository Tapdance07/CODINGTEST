n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() 
B_indexed = list(enumerate(B))
B_indexed.sort(key=lambda x: x[1], reverse=True)


result = [0] * n
for i in range(n):
    idx = B_indexed[i][0]
    result[idx] = A[i]


answer = sum(result[i] * B[i] for i in range(n))
print(answer)
