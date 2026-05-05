def solution(board, moves):
    answer = 0
    stack = [0]  
    
    for n in moves:
        column_index = n - 1 
        
        for row in board:  
            if row[column_index] != 0:
                doll = row[column_index]
                row[column_index] = 0 
                
                if stack[-1] == doll:
                    stack.pop()
                    answer += 2  
                else:
                    stack.append(doll)
                
                break 
                
    return answer