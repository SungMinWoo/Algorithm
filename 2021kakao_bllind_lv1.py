import re

def solution(new_id):
    answer = ''
    new_list = []
    new_id = new_id.lower().replace(' ', '') # 소문자로 치환 공백 제거
    new_id = re.sub(r'[^a-z0-9._-]', '', new_id) # 특수 문자 제거

    for a in range(len(new_id)): # 연속된 . 제거
        if a == len(new_id) - 1:
            new_list.append(new_id[a])
        elif new_id[a] == '.':
            if new_id[a] != new_id[a + 1]:
                new_list.append(new_id[a])
        else:
            new_list.append(new_id[a])
    new_id = ''.join(new_list)

    new_id = new_id.strip('.') # 양끝 . 제거
    if len(new_id) == 0: # 값이 없을 경우 a로 치환
        new_id = 'a'
    if len(new_id) >= 16: # 길이가 15로 치환
        answer = new_id[:15]
    elif len(new_id) <= 2: # 값의 길이가 2이하면 그에 맞게 같은 문자 추가
        answer = new_id + (new_id[len(new_id) - 1] * (3 - len(new_id)))
    else:
        answer = new_id

    return answer.strip('.')