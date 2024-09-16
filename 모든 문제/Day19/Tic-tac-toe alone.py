def won(board, t):
    for row in board:
        if row == [t, t, t]:
            return True
    
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True
    
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
        return True
    
    return False

def solution(board):
    board = [list(row) for row in board]

    o_count, x_count = 0, 0
    for row in board:
        for c in row:
            if c == 'O':
                o_count += 1
            if c == 'X':
                x_count += 1
    
    if not (o_count == x_count or o_count == x_count + 1):
        return 0
    
    if won(board, 'O') and won(board, 'X'):
        return 0
    
    if won(board, 'O') and o_count != x_count + 1:
        return 0
    if won(board, 'X') and o_count != x_count:
        return 0
    
    return 1