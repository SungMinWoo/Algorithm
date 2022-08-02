def solution(numbers, hand):
    answer = ''
    left = 4
    right = 4
    keypad = {'L': [1, 4, 7], 'R': [3, 6, 9], 'C': [2, 5, 8, 0]}
    for a in numbers:
        if a in keypad['L']:
            answer += 'L'
            left = keypad['L'].index(a)
        elif a in keypad['R']:
            answer += 'R'
            right = keypad['R'].index(a)
        elif a in keypad['C']:
            test = keypad['C'].index(a)
            if test - left == test - right:
                answer += hand[0].upper()
                if hand[0].upper() == 'R':
                    right = test
                else:
                    left = test
            elif test - left > test - right:
                answer += 'R'
                right = test
            elif test - right > test - left:
                answer += 'L'
                left = test
    return answer