def solution(n, lost, reserve):
    if list(set(lost) & set(reserve)) != 0:
        new_lost = list(set(lost) - set(reserve))
        new_reserve = list(set(reserve) - set(lost))
    else:
        new_lost = lost
        new_reserve = reserve
    new_reserve.sort()
    new_lost.sort()
    answer = n - len(new_lost)
    for b in new_reserve:
        for a in new_lost:
            new_list = [a - 1, a, a + 1]
            if b in new_list:
                answer += 1
                new_lost.remove(a)
                break
    return answer