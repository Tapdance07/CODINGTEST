white = [[0 for j in range(100)] for i in range(100)]
S = int(input())
T = 0

for i in range(S):
    A , B = map(int,input().split())
    for z in range(10):
        for x in range(10):
            if white[A+z][B+x] == 0:
                white[A+z][B+x] = 1
                T +=1
            else:
                pass

print(T)