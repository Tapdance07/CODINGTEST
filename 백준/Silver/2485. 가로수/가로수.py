import sys

T = int(sys.stdin.readline().rstrip())
S = list()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for i in range(T):
    S.append(int(sys.stdin.readline().rstrip()))

#초기 세팅
gap = [S[i]- S[i-1] for i in range(1,T)]

current_gcd = gap[0]

for gaps in gap:
    current_gcd = gcd(current_gcd,gaps)

additional_trees = sum(gaps // current_gcd - 1 for gaps in gap)
print(additional_trees)