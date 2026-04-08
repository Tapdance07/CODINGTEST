total = int(input())
co = int(input())
sums = 0
for i in range(co):
    a,b = map(int,input().split())
    sums += (a*b)

if sums==total:
    print("Yes")
else:
    print("No")