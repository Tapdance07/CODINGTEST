import sys

T = int(sys.stdin.readline().rstrip())  # 테스트 케이스의 개수

for _ in range(T):
    VPS_T = list(sys.stdin.readline().rstrip())  # 괄호 문자열
    stack = []  # 스택을 사용하여 괄호 쌍을 확인

    for char in VPS_T:
        if char == '(':  # '('이면 스택에 추가
            stack.append(char)
        elif char == ')':  # ')'이면 스택에서 하나 꺼내기
            if stack:  # 스택에 '('가 있다면 하나 꺼내고 짝을 맞춤
                stack.pop()
            else:  # 스택이 비어있다면 짝이 맞지 않으므로 NO 출력
                print('NO')
                break
    else:
        # 괄호 문자열 끝까지 확인 후 스택에 남아있는 괄호가 없으면 YES, 있으면 NO
        if stack:
            print('NO')
        else:
            print('YES')