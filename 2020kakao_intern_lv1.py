def solution(numbers, hand):
    answer = ''
    left = [0, 3] # 초기 위치
    right = [2, 3]
    keypad = {'L': [1, 4, 7, '*'], 'R': [3, 6, 9, '#'], 'C': [2, 5, 8, 0]} # 키보드 딕셔너리
    for number in numbers:
        if number in keypad['L']: # 왼손
            answer += 'L'
            left = [0, keypad['L'].index(number)] # 좌표 저장
        elif number in keypad['R']: # 오른손
            answer += 'R'
            right = [2, keypad['R'].index(number)]
        elif number in keypad['C']:
            num_posi = [1, keypad['C'].index(number)]
            right_posi = abs(num_posi[0] - right[0]) + abs(num_posi[1] - right[1]) # 손가락 위치랑 숫자 중앙 숫자 위치 계산
            left_posi = abs(num_posi[0] - left[0]) + abs(num_posi[1] - left[1])

            if left_posi > right_posi: # 값이 적을 수록 가까움
                answer += 'R'
                right = num_posi
            elif right_posi > left_posi:
                answer += 'L'
                left = num_posi
            else: # 같을 때는 주요 손의 손가락이 나감
                answer += hand[0].upper()
                if hand[0].upper() == 'R':
                    right = num_posi
                else:
                    left = num_posi
    return answer