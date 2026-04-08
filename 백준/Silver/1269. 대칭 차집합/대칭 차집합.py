import sys

A,B = map(int,sys.stdin.readline().split())
A_Set = set(map(int,sys.stdin.readline().split()))
B_Set = set(map(int,sys.stdin.readline().split()))

A_Set_dirr = A_Set - B_Set
B_Set_dirr = B_Set - A_Set

print(len(A_Set_dirr)+len(B_Set_dirr))