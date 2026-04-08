C = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
T = input()

Count = 0
i = 0

while i < len(T):
    if T[i:i+3] in C:
        Count += 1
        i += 3
    elif T[i:i+2] in C:
        Count += 1
        i += 2

    else:
        Count += 1
        i += 1

print(Count)