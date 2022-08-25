from itertools import combinations


def solution(numbers, target):
    answer = 0
    reverse_numbers = list(reversed(numbers))

    for num in range(1, (len(numbers)//2)):
        combi_num = list(combinations(numbers, num))
        test = list(combinations(reverse_numbers, len(numbers) - num))
        for count in range(len(combi_num)):
            if sum(test[count]) - sum(combi_num[count]) == target:
                answer += 1
    return answer