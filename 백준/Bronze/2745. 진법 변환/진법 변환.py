dic = {}
for i in range(26):
    dic[chr(65+i)]=i+10

N, B = input().split()
B = int(B)
A = list(N)
total = 0
for i in range (len(A)):
    if A[-i-1] not in dic:
        total += int((A[-i-1])) * B ** i
    else:
        total += int(dic[(A[-i-1])]) * B ** i
print(total)
