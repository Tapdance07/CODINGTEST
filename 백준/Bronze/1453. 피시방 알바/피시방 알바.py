N = int(input())
S = list(map(int,input().split()))
T = set(S)
print((len(S)-len(T)))