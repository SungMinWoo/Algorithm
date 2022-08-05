def solution(board, moves):
    answer = 0
    result = []
    for move in moves:
        count = 0
        for a in board:
            if a[move-1] == 0: # 값이 0이면 넘어감
                count += 1
                pass
            else:
                result.append(a[move - 1]) # 리스트에 담음
                board[count][move - 1] = 0 # board에서 리스트에 담은 값 삭제
                if len(result) == 0 or len(result) == 1:
                    pass
                elif result[-1] == result[-2]:
                    answer += 2
                    del result[-2:] # 원래 del -1 del -2 였는데 삭제를 잘못하고 있었음
                break
    return answer