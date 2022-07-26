def solution(s):
    char_dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

    for a in list(char_dic.keys()):
        if a in s:
            s = s.replace(a, char_dic[a])

    return int(s)