import math
from itertools import combinations

def solution(nums):
    answer = 0
    comb_list = list(combinations(nums, 3))
    for j in comb_list:
        for i in range(2, int(math.sqrt(sum(j)))+1):
            if sum(j) % i == 0:
                answer += 1
                break

    return len(comb_list) - answer