# KAKAO Algorithm Code Review

# Problem 1

# Problem 2
  1. 올바른 괄호 문자열 자체를 **참**으로 인식하기 때문에 따로 구하는 함수를 만들 필요가 없다.
  ```
  retrun u + solution(v) if isRight(u) else createNewString(u, v)
  ```
  isRight()으로 stack을 활용해 올바른 괄호 문자열인지 확인했지만, 아래 코드와 같이 수정할 수 있다.
  ```
  return u + solution(v) if u else createNewString(u, v)
  ```  
  
  2. 문자열 부분 수정은 지원하지 않으므로 새로운 문자열을 만들어야 한다.
  ```
  something[3] = 'z'
  ```
  위의 코드처럼 수행할 경우 오류가 발생하여 아래와 같이 수행해야 한다.
  ```
  somethingNew = something[:3] + 'z' + something[4:]
  ```
  
  3. 문자열의 마지막 인덱스부터 슬라이싱하는 경우 빈 문자열을 반환한다.
  ```
  return something[i:] if not i == len(something) - 1 else ""
  ```
  위의 코드처럼 수행할 필요없이 아래와 같이 수행해도 된다.
  ```
  return something[i:]
  ```
  
# Problem 3

# Problem 4

# Problem 5

# Problem 6

# Problem 7
