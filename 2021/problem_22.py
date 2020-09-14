from collections import Counter
from itertools import combinations

def solution(orders, course) -> list:
    # 2 <= len(orders) <= 20
    # 2 <= order <= 10, only uppercase and no duplication
    # 2 <= len(course) <= 10, asending, no duplication
    answer = []

    # 주문 별 코스 개수로 묶기
    orders = [[list(map(''.join, combinations(sorted(order), number))) for order in orders] for number in course]
 
    # 2차원 리스트로 변경
    orders = [[course for courses in order for course in courses] for order in orders]
  
    # 주문 최대 개수 확인
    for order in orders:
        values = Counter(order).values()
        if not values: continue
        maximum = max(values) 

        # 코스가 두 번 이상 주문되었다면 저장
        if maximum >= 2:
            answer += [course for course, count in Counter(order).most_common() if count == maximum]

    # 오름차순 정렬 후 반환
    return sorted(answer)



print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))