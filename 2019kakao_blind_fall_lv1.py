def solution(N, stages):
    answer = {}
    sum_stages = 0
    for i in range(1, N+1):
        if len(stages)-sum_stages == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i)/(len(stages)-sum_stages)
        sum_stages += stages.count(i)
    answer = {k: v for k, v in sorted(answer.items(), key=lambda item: item[1], reverse=True)}

    return list(answer.keys()) # 3000mm