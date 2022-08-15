def solution(answers):
    answer = []
    last_answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first *= 8
    second *= 5
    third *= 4
    count, len_answer, first_count, second_count, third_count = 0, 0, 0, 0, 0

    while True:

        if answers[len_answer] == first[count]:
            first_count += 1

        if answers[len_answer] == second[count]:
            second_count += 1

        if answers[len_answer] == third[count]:
            third_count += 1

        count += 1
        len_answer += 1
        if count == 40:
            count -= 40

        if len_answer == len(answers):
            answer = [first_count, second_count, third_count]
            break

    max_index = max(answer)
    for i, v in enumerate(answer): # tuple 형태로 반환하여 value값으로 index를 찾을 수 있음
        if v == max_index:
            last_answer.append(i+1)
    return sorted(last_answer)