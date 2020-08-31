RIGHT = -1
LEFT = 1
UP = 1
DOWN = -1
is_possible = False

def solution(key, lock):
    for _ in range(4):
        moveKey(0, 0, key, lock, [])
        key = turn(key)
        print('turn')

    return isPossible

def turn(key):
    return [[key[y][x] for y in range(len(key) - 1, -1, -1)] for x in range(len(key))]

def moveKey(to_y, to_x, key, lock, check_board):
    global isPossible

    if isPossible: return

    new_key = [[0 for _ in range(len(lock))] for _ in range(len(lock))]

    for y in range(len(key)):
        for x in range(len(key)):
            if key[y][x] == 1:
                if -1 < y + to_y and y + to_y < len(new_key) and -1 < x + to_x and x + to_x < len(new_key):
                    new_key[y + to_y][x + to_x] = 1

    temp = [new_key[y][x] for y in range(len(new_key)) for x in range(len(new_key))]
    if temp in check_board: return 

    check_board.append(temp)

    print('- ' * 10)
    print('\n'.join(map(str, new_key)))

    if isRightKey(new_key, lock):
        is_possible = True    
        return
    
    moveKey(to_y + UP, to_x, key, lock, check_board)
    moveKey(to_y + DOWN, to_x, key, lock, check_board)
    moveKey(to_y, to_x + RIGHT, key, lock, check_board)
    moveKey(to_y, to_x + LEFT, key, lock, check_board)

def isRightKey(key, lock):
    for y in range(len(lock)):
        for x in range(len(lock)):
            if not key[y][x] + lock[y][x] == 1: 
                return False

    return True

print(solution([[0, 0, 0], [0, 0, 0], [0, 1, 1]], [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))

"""
    lock이 모두 1인 경우 -> key를 모두 0으로 하면 풀리도록 하는 반례가 있어서 오래 걸림
    key와 lock의 길이가 같은 경우로만 생각 -> 그렇지 않음
"""
