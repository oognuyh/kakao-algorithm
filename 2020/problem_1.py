from math import ceil

def solution(s):   
    for splited_count in range(1, ceil(len(s) / 2) + 1): # 문자열의 중간 길이까지를 단위로 비교
        string = [s[i:i + splited_count] for i in range(0, len(s), splited_count)] # 단위로 문자열을 잘라 리스트로 변환

        stack = []

        for word in string: # 같은 값이 연속해서 나타나는 경우를 스택을 통해 확인
            if stack: # stack = [count, 'word' .. ]
                if stack[-1] == word:
                    stack[-2] += 1                                    
                else:
                    stack.append(1)
                    stack.append(word)
            else:
                stack.append(1)
                stack.append(word)

        for i in range(0, len(stack), 2): # 한 번만 반복된 상수 확인
            if stack[i] < 2: stack[i] = '*'

        length = ''.join(map(str, stack)) # 연속된 값 체크한 스택을 문자열로 변환
        length = len(length.replace('*', '')) # 한 번만 반복된 경우 상수 제거

        answer = length if splited_count == 1 else length if answer > length else answer # 최솟값인지 확인

    return answer
