def solution(numbers, target):
    answer = [0]
    result = []
    def dsf(i, l, n):
        tmp = []
        if i == len(n):
            result.append(l.count(target))
            return
        else:
            for j in l:
                tmp.append(j+n[i])
                tmp.append(j-n[i])
            answer = tmp
            dsf(i + 1, answer, n)
    dsf(0, answer, numbers)

    return result[0]