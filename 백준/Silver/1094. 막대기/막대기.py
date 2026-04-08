import sys
stick = list()

X = int(sys.stdin.readline())
while X >1:
    stick.append(X % 2)
    X = X//2
stick.append(1)
print(stick.count(1))


