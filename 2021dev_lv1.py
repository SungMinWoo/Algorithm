def change(count):
    if count == 6:
        count = 1
    elif count == 5:
        count = 2
    elif count == 4:
        count = 3
    elif count == 3:
        count = 4
    elif count == 2:
        count = 5
    else:
        count = 6
    return count


def solution(lottos, win_nums):
    answer = []
    count_zero = lottos.count(0)
    count = 0

    for lot in lottos:
        for win in win_nums:
            if lot == win:
                count += 1
            else:
                continue
    top_lot = count + count_zero

    answer = [change(top_lot), change(count)]
    return answer