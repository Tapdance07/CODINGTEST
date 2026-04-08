import sys


while 1:
    T = list(sys.stdin.readline().rstrip())

    if T[0] == '.':
        break

    Stack = []

    for i in range(len(T)):
        if T[i] == '(' or T[i] == '[':
            Stack.append(T[i])
        elif T[i] == ')' :
            if len(Stack) >0 and Stack[-1]=='(':
                Stack.pop()
            else:
                print('no')
                break
        elif T[i] == ']':
            if len(Stack) > 0 and Stack[-1]=='[':
                Stack.pop()
            else:
                print('no')
                break
        elif T[i] == '.':
            if len(Stack)==0:
                print('yes')
            else:
                print('no')
            break

