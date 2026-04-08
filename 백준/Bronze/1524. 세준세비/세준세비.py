T = int(input())

for _ in range(T):
    input() 
    N, M = map(int, input().split())
    sejun = list(map(int, input().split()))
    sebi = list(map(int, input().split()))

    if max(sejun) >= max(sebi):
        print('S')
    else:
        print('B')
