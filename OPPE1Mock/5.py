'''
Question's too long
'''

def row_pattern(board, r):
    return board[r]
    
def col_pattern(board, c):
    L = [ ]
    for i in range(len(board)):
        L.append(board[i][c])
    return L
            
def main_diag_pattern(board):
    L = [ ]
    for i in range(len(board)):
        L.append(board[i][i])
    return L
    
def anti_diag_pattern(board):
    L = [ ]
    for i in range(len(board)):
        L.append(board[i][-i-1])
    return L

def tic_tac_toe(board):
    patterns = [ ]
    for i in range(len(board)):
        patterns.append(row_pattern(board, i))
        patterns.append(col_pattern(board, i))
    patterns.append(main_diag_pattern(board))
    patterns.append(anti_diag_pattern(board))
        
    for pattern in patterns:
        if pattern == ['X'] * len(board):
            return 'X'
        elif pattern == ['O'] * len(board):
            return 'O'
    return -1
