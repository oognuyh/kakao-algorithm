def solution(p):
    if p == "": return p # 빈 문자열인 경우, 빈 문자열을 반환
    
    u, v = split(p) # 균형잡힌 괄호 문자열 u, v로 분리 v는 빈 문자열 가능하며 u는 더 이상 분리 불가
        
    return u + solution(v) if isRight(u) else createNewString(u, v) # 올바른 경우라면 문자열 v에 대해 다시 수행 후 u에 붙이며, 아닐 경우 새로운 문자열 생성

def createNewString(u, v):      
    # 첫 번째 문자로 '('를 넣고 v에 대해 1단계부터 재귀적으로 수행하여 붙이고 ')'를 붙인다. 
    # 이후 u의 첫 번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 붙여 반환한다.
    return '(' + solution(v) + ')' + ''.join(list(map(lambda x : ')' if x == '(' else '(', u[1:-1])))

def isRight(u):
    # u에 대해 올바른 괄호 문자열인지 확인한다.
    stack = []
    
    for c in u:
        if stack:
            if stack[-1] == '(':
                stack.pop() if c == ')' else stack.append(c)
        else:
            if c == ')': return False
            stack.append(c) 
    
    return False if stack else True

def split(p):
    # 문자열 p에 대해 두 균형잡힌 괄호 문자열로 분리한다.
    # u는 더 이상 분리가 불가능하여 처음 균형잡힌 괄호 문자열로 분리되었을 때 반환한다.
    right, left = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(': right += 1 
        else: left += 1
        if right == left:
            u = p[:i + 1]
            v = p[i + 1:] 
            return u, v
