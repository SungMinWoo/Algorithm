def solution(queue1, queue2):
    answer = -2
    sum_queue = sum(queue1 + queue2)
    queue_list = range(int(sum_queue/2), sum_queue+1)
    if set(queue_list) & set(queue1 + queue2):
        return -1
    else:
        while True:
            queue1.pop()
            return answer