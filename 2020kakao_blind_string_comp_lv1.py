def solution(s):
    split_list = []
    result = []
    for count in range(1, len(s)):
        test = [s[i:i + count] for i in range(0, len(s), count)]
        split_list.append(test)
        result.append(len(s))

    count = 0
    for split in split_list: # 갯수 별로 자른 리스트
        for sp in range(0, len(split)-1): # 내부 리스트
            if len(split) == 2:
                if split[sp] == split[sp + 1]:
                    result[count] -= len(split[sp])
                    result[count] += 1
            else:
                if split[sp] == split[sp-1] and split[sp] == split[sp+1]:
                    result[count] -= len(split[sp])
                elif split[sp] == split[sp+1]:
                    result[count] -= len(split[sp])
                    result[count] += 1
        count += 1
    return min(result)