dic = {}
for i in range(26):
    dic[i+10]=chr(65+i)
N , B = map(int,input().split())
T = list()

while N >= B:

    if N%B > 9:
        T.append(dic[(N % B)])
    else:
        T.append(N % B)
    N = N // B


if N > 9:
    T.append(dic[N])
else:
    T.append(N)

for i in range(len(T)):
    print((T[-i-1]),end='')