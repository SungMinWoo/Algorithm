def solution(record):
    answer = []
    id_list = {}
    for i in record:
        if i.split()[0] != 'Leave':
            id_list[i.split()[1]] = i.split()[2]

    for log in record:
        if log.split()[0] == 'Enter':
            answer.append(f"{id_list[log.split()[1]]}님이 들어왔습니다.")
        elif log.split()[0] == 'Leave':
            answer.append(f"{id_list[log.split()[1]]}님이 나갔습니다.")

    return answer