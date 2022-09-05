import re

def solution(str1, str2):
    answer = 0
    str1_list = []
    str2_list = []
    str1, str2 = str1.lower(), str2.lower()
    if max(str1) >= max(str2):
        max_len = len(str1)
    else:
        max_len = len(str2)
    for a in range(1, max_len+1):
        re_str1 = re.sub('[^a-z]', '', str1[a-1:a+1])
        re_str2 = re.sub('[^a-z]', '', str2[a-1:a+1])
        if re_str1 == re_str2 and len(re_str2) == 2:
            answer += 1
        if len(re_str1) == 2:
            print(str1[a - 1:a + 1])
            str1_list.append(str1[a - 1:a + 1])
        if len(re_str2) == 2:
            str2_list.append(str2[a - 1:a + 1])

    # return int((len(set(str2_list)&set(str2_list)) / len(set(str2_list)|set(str2_list))) * 65536)
    if answer == 0 or len(set(str1_list + str2_list)) == 0:
        return 65536
    else:
        return int((answer / len(set(str1_list + str2_list))) * 65536)