a,b = map(int,input().split())
tum = int(input())
b+= tum
if b>59:
    a+=(b//60)
    b%=60
    if a>23:
        a-=24

print(a,b)
