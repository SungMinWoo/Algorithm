def solution(s):
    answer = True
    stack = []
    for a in s:
        if a == '(':
            stack.append(a)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        answer = False
    return answer