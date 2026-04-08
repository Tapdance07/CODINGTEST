import sys

N = int(sys.stdin.readline())
Deck = list()
for _ in range(N):
    Input = sys.stdin.readline().split()
    if Input[0] == "push_front":
        Deck.insert(0,Input[1])
    elif Input[0] == "push_back":
        Deck.append(Input[1])
    elif Input[0] == "pop_back":
        if len(Deck) > 0:
            print(Deck.pop())
        else:
            print(-1)
    elif Input[0] == "pop_front":
        if len(Deck) > 0:
            print(Deck.pop(0))
        else:
            print(-1)
    elif Input[0] == "size":
        print(len(Deck))
    elif Input[0] == "empty":
        if len(Deck) == 0:
            print(1)
        else:
            print(0)
    elif Input[0] == "front":
        if len(Deck) > 0:
            print(Deck[0])
        else:
            print(-1)
    elif Input[0] == "back":

        if len(Deck) > 0:
            print(Deck[-1])
        else:
            print(-1)












