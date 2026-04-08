import sys

board = sys.stdin.readline().rstrip()
board += '.'
result = ""
count = 0

for i in range(len(board)):
    if board[i] == 'X':
        count += 1
    else:

        if count % 2 != 0:
            print(-1)
            sys.exit()  


        result += 'AAAA' * (count // 4)
        result += 'BB' * ((count % 4) // 2)
        if i < len(board) - 1:
            result += '.'
        count = 0

print(result)