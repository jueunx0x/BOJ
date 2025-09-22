def solution(board, moves):
    answer = 0
    doll = []
    count = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0 :
                continue
            else:
                doll.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(doll) > 1 :
            if doll[-1] == doll[-2]:
                count+=2
                doll.pop()
                doll.pop()
                
    answer = count
    return answer