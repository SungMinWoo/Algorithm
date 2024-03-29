from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    queue12 = queue1 + queue2
    last_sum = sum(queue12) // 2

    sum_queue = sum(queue1)
    while answer < len(queue12) * 2:
        if sum_queue == last_sum:
            break
        elif sum_queue > last_sum:
            pop_left = queue1.popleft()
            queue2.append(pop_left)
            sum_queue -= pop_left
            answer += 1
        elif sum_queue < last_sum:
            pop_left = queue2.popleft()
            queue1.append(pop_left)
            sum_queue += pop_left
            answer += 1

    if answer >= len(queue12) * 2:
        return -1
    else:
        return answer