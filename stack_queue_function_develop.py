import math

def solution(progresses, speeds):
    answer = []
    result = []
    for count in range(len(progresses)):
        answer.append(math.ceil((100 - progresses[count]) / speeds[count]))
    a = 0
    while a <= len(answer)-1:
        if len(answer) == sum(result):
            break
        result_num = 1
        answer_a = answer[a]
        for b in range(a+1, len(answer)):
            if answer_a >= answer[b]:
                result_num += 1
                a += 1
            else:
                break
        result.append(result_num)
        a += 1
    return result