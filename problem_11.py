def solution(new_id) -> str:
    alphabets = list(map(chr, range(97, 123)))
    numbers = list(map(str, range(0, 10)))
    specials = ['-', '_', '.']

    # 소문자로 변경 후 숫자, 알파벳, 허용된 특수기호가 아닌 경우 제거
    new_id = [character for character in new_id.lower() if character in alphabets or 
                                                           character in numbers or
                                                           character in specials]
    
    # 마침표 제거
    new_id = remove_period(new_id)

    # 빈 문자열인지 확인
    if not new_id:
        new_id = 'a'
    
    # 길이가 16자 이상이라면 자르기 제거 후 마침표가 끝에 있다면 제거
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')
    # 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복해서 붙이기
    elif len(new_id) < 3:
        new_id = new_id + new_id[-1] * (3 - len(new_id))

    answer = ''.join(new_id)

    return answer

def remove_period(new_id) -> str:
    new_id = ''.join(new_id)
    # 연속된 마침표 축소
    for count in range(len(new_id), 1, -1):
        new_id = new_id.replace("." * count, '.')
    
    # 처음과 끝이 마침표라면 제거 후 반환
    return new_id.strip('.') 

print(solution("...!@BaT#*..y.abcdefghijklm"))


