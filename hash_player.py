import collections

def solution(participant, completion):
    answer = collections.Counter(input1) - collections.Counter(input2)
    return list(answer.keys())[0]