A, B, V = map(int,input().split())


if A != V:
    if V-B != A:
        V = V - B
        T = A - B
    else:
        T = A - B
    if (V/T)%1 > 0:
        print((V//T)+1)
    else:
        print(V // T)
else:
    print(1)