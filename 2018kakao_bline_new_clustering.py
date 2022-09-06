def solution(str1, str2):
    str1_list = []
    str2_list = []
    count = 0
    str1, str2 = str1.lower(), str2.lower()
    for b in range(len(str1) - 1):
        if str1[b:b + 2].isalpha():
            str1_list.append(str1[b:b + 2])
    for b in range(len(str2) - 1):
        if str2[b:b + 2].isalpha():
            str2_list.append(str2[b:b + 2])

    for b in str1_list:
        if b in str2_list:
            count += 1
            str2_list.remove(b)

    all_list = len(str1_list + str2_list) - count

    if count == 0 and all_list != 0:
        return 0
    elif count == 0 or all_list == 0:
        return 65536
    else:
        return int(count / all_list * 65536)