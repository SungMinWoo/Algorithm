def solution(s):
    split_list = []
    result = []
    for count in range(1, len(s)):
        test = [s[i:i + count] for i in range(0, len(s), count)]
        split_list.append(test)
        result.append(len(s))

    for split in range(len(split_list)): # 갯수 별로 자른 리스트
        for sp in range(len(split_list[split])-1): # 내부 리스트
            try:
                if split_list[split][sp] == split_list[split][sp+1] and split_list[split][sp] == split_list[split][sp-1]:
                    result[split] -= len(split_list[split][sp])
                elif split_list[split][sp] == split_list[split][sp+1]:
                    result[split] -= len(split_list[split][sp])
                    result[split] += 1
            except:
                continue
    return min(result)