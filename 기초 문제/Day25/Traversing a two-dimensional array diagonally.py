def solution(board, k):
    answer = 0

    for i in range(min(k + 1, len(board))):
        for j in range(min(k + 1 - i, len(board[i]))):
            answer += board[i][j]
    
    return answer