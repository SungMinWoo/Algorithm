from itertools import combinations

def solution(orders, course):
    new_list = []
    combi = []
    result = []
    course_list = []
    answer = []
    if len(set(orders)) == 1:
        answer = []
        new_lists = []
        for a in course:
            new_lists.append(combinations(orders[0],a))

        for a in new_lists:
            for b in a:
                answer.append(''.join(b))
        return sorted(set(answer))
    else:
        for a in range(len(orders)):
            new_list.append([]) # orders의 길이 만큼 빈 list 생성
            combi.append(a) # orders의 반복만큼 정수 list 생성
            for i in orders[a]:
                new_list[a].append(i) # order의 문자열을 2차원 리스트로 변환

        for i in list(combinations(combi, 2)): # orders의 모든 조합 생성
            a = ''.join(sorted(set(new_list[i[0]]) & set(new_list[i[1]]))) # 조합마다 모든 리스트 비교 및 정렬 후 문자열로 전환
            if len(a) in course:
                result.append([a, i[0]])
                course_list.append(i[0])

        for a in set(course_list): # course_list 중복값 제거
            result_len_list = []
            for b in result:
                if b[1] == a: # result 2차원 리스트의 1번째 값이 같은 번호로 주문한 사람이라면
                    result_len_list.append(len(b[0])) # 같은 번호의 문자열 리스트를 담음
            max_result_len = max(result_len_list) # 문자열 중 가장 빈도수가 많은 값
            for d in result:
                if len(d[0]) == max_result_len and d[1] == a: # 길이가 가장 길고 같은 번호로 주문한 사람이면
                    answer.append(d[0])

        return sorted(set(answer))